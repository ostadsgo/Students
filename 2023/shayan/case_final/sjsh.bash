#!/bin/bash

# Colors
RED='\033[0;31m'
RESET='\033[0m'

function print_header() {
    echo "***********************************************************"
    echo "		SYSTEM MANAGER (version 1.0.0)"
    echo "-----------------------------------------------------------"
}

function print_menu() {
    clear
    echo "***********************************************************"
    echo -e "\t\tSYSTEM MANAGER (version 1.0.0)"
    echo "-----------------------------------------------------------"
    echo -e "${RED}ni${RESET} - Network Info    (Network information)\n"
    echo -e "${RED}ua${RESET} - User Add        (Create a new user)"
    echo -e "${RED}ul${RESET} - User List       (List all login users)"
    echo -e "${RED}uv${RESET} - User View       (View user properties)"
    echo -e "${RED}um${RESET} - User Modify     (Modify user properties)"
    echo -e "${RED}ud${RESET} - User Delete     (Delete a login user)\n"
    echo -e "${RED}ga${RESET} - Group Add       (Create a new group)"
    echo -e "${RED}gl${RESET} - Group List      (List all groups, not system groups)"
    echo -e "${RED}gv${RESET} - Group View      (List all users in a group)"
    echo -e "${RED}gm${RESET} - Group Modify    (Add/remove user to/from a group)"
    echo -e "${RED}gd${RESET} - Group Delete    (Delete a group, not system groups)\n"
    echo -e "${RED}fa${RESET} - Folder Add      (Create a new folder)"
    echo -e "${RED}fl${RESET} - Folder List     (View content in a folder)"
    echo -e "${RED}fv${RESET} - Folder View     (View folder properties)"
    echo -e "${RED}fm${RESET} - Folder Modify   (Modify folder properties)"
    echo -e "${RED}fd${RESET} - Folder Delete   (Delete a folder)\n"
    echo -e "${RED}ex${RESET} - Exit            (Exit System Manager)"
    echo "-----------------------------------------------------------"
}

# Main loop of the script
while true; do
    print_menu
    read -rp "Choice: " user_choice

    case $user_choice in
        ni)
            clear
            print_header
            computer_name=$(uname -n)
            ip_addr=$(ip a | grep "inet " | sed -n '2p' | cut -c 10-20)
            getway=$(ip route | awk '/default/ {print $3}')
            up_interface=$(ip route | grep default | awk '{print $5}')
            mac_addrs=$(ip link show | awk '/link\/ether/ {print $2}')
            status=$(ip -o link show "$up_interface" | awk '{print $9}')
            echo -e "${RED}Computer name:${RESET}${NC} $computer_name"
            echo -e "${RED}Interface:${RESET}${NC} $up_interface"
            echo -e "${RED}Ip Address:${RESET}${NC} $ip_addr"
            echo -e "${RED}Getway:${RESET}${NC} $getway"
            echo -e "${RED}MAC:${RESET}${NC} $mac_addrs"
            echo -e "${RED}Status:${RESET}${NC} $status"
            echo "-----------------------------------------------------------"
            ;;

        ua)
            clear
            print_header
            echo "Enter the user name: "
            read -r username
            sudo adduser "$username"
            echo "User $username created successfully."
            ;;
        ul)
            clear
            print_header
            echo ""
            echo "List of Users"
            echo "------------------------------------------------------------"
            list_users=$(getent passwd | cut -d: -f1,7 | grep -E '/bash$|/sh$' | cut -d: -f1)
            echo "$list_users" | tr ' ' '\n'
            echo ""
            ;;

        uv)
            clear
            print_header
            read -rp "enter username to view: " user

            passwd_line=$(grep "$user" /etc/passwd)
            echo ""

            # Dela upp raden och lagra varje del i en separat variabel
            IFS=':' read -r username password uid gid fullname home shell <<< "$passwd_line"
            echo "Properties for user: $user"
            echo ""
            echo -e "\e[31mUser:\e[0m         $username"
            echo -e "\e[31mPassword:\e[0m     $password"
            echo -e "\e[31mUser-ID:\e[0m      $uid"
            echo -e "\e[31mGroup-ID:\e[0m     $gid"
            echo -e "\e[31mComment:\e[0m      $fullname"
            echo -e "\e[31mDirectory:\e[0m    $home"
            echo -e "\e[31mShell:\e[0m        $shell"
            echo ""
            echo -e "\e[31mGroups:\e[0m       $(id -nG $user | tr ' ' ',')"
            echo "-----------------------------------------------------------"
            ;;

        um)
            clear
            echo -e "${RED}sa${RESET} - Show attributes"
            echo -e "${RED}ea${RESET} - Edit attributes"
            echo -e "${RED}cu${RESET} - Change username"
            echo -e "${RED}cp${RESET} - Change password"

            echo ""

            read -p "choice: " you
            case $you in
                sa)
                    clear
                    read -p "Show attributes for: " name
                    if id "$name" >/dev/null 2>&1
                    then
                        PASSWD_STRING=$(grep "^$name:" /etc/passwd)
                        USERID=$(echo "$PASSWD_STRING" | cut -d: -f3)
                        PRIMARY_GID=$(echo "$PASSWD_STRING" | cut -d: -f4)
                        PRIMARY_GROUP=$(getent group "$PRIMARY_GID" | cut -d: -f1)
                        GECOS=$(echo "$PASSWD_STRING" | cut -d: -f5)
                        HOMEDIR=$(echo "$PASSWD_STRING" | cut -d: -f6)
                        HOMESHELL=$(echo "$PASSWD_STRING" | cut -d: -f7)

                        echo -e "\n\e[1mUSERNAME\e[0m: $name"
                        echo -e "\e[1mUSER ID\e[0m: $USERID"
                        echo -e "\e[1mPRIMARY GROUP\e[0m: $PRIMARY_GROUP ($PRIMARY_GID)"
                        echo -e "\e[2mALL GROUPS\e[0m: $(id "$name" | cut -d' ' -f3 | cut -b 8-)"
                        echo -e "\e[1mGECOS\e[0m: $GECOS"
                        echo -e "\e[1mHOME DIRECTORY\e[0m: $HOMEDIR"
                        echo -e "\e[1mDEFAULT SHELL\e[0m: $HOMESHELL"
                    else
                        echo "User $name not found."
                    fi
                    ;;
                ea)
                    clear
                    echo -e "${RED}1${RESET} - Change GECOS (comment)"
                    echo -e "${RED}2${RESET} - Change Home Directory"
                    echo -e "${RED}3${RESET} - user id (comment)"
                    echo -e "${RED}4${RESET} - group id (comment)"
                    echo -e "${RED}5${RESET} - default shell (comment)"
                    echo -e "${RED}0${RESET} - Back to main menu"

                    read -p "Enter option: " edit_option
                    read -p "user: " name
                    case $edit_option in
                        1)
                            read -p "Enter new GECOS: " new_gecos
                            sudo usermod -c "$new_gecos" "$name"
                            if [ $? -eq 0 ]; then
                                echo "GECOS changed to: $new_gecos"
                            else
                                echo "Failed to change GECOS."
                            fi
                            ;;
                        2)
                            read -p "Enter new home directory: " new_homedir
                            sudo usermod -d "$new_homedir" -m "$name"
                            if [ $? -eq 0 ]; then
                                echo "Home directory changed to: $new_homedir"
                            else
                                echo "Failed to change home directory."
                            fi
                            ;;
                        3)
                            read -p "Enter new User ID: " new_uid
                            if id -u "$new_uid" &>/dev/null; then
                                echo "it's already used $new_uid"

                            elif [$new_uid -le 1000 ]; then
                                echo "the UID should be bigger then 1000"
                            else
                                sudo usermod -u "$new_uid" "$name"
                                if [ $? -eq 0 ]; then
                                    echo "User ID changed to: $new_uid"

                                else
                                    echo "Failed to change User ID."
                                fi
                            fi

                            ;;
                        4)
                            read -p "Enter new Group ID: " new_gid
                            sudo usermod -g "$new_gid" "$name"
                            if [ $? -eq 0 ]; then
                                echo "Group ID changed to: $new_gid"
                            else
                                echo "Failed to change Group ID."
                            fi
                            ;;
                        5)
                            read -p "Enter new Default Shell: " new_shell
                            sudo usermod -s "$new_shell" "$name"
                            if [ $? -eq 0 ]; then
                                echo "Default Shell changed to: $new_shell"
                            else
                                echo "Failed to change Default Shell."
                            fi
                            ;;


                        0)
                            ;;
                        *)
                            echo "Invalid option."
                    esac
                    ;;



                cu)
                    read -p "which username: " user_modify
                    if id "$user_modify" > /dev/null 2>&1
                    then
                        read -p "write the new username: " new_user
                        sudo usermod -l $new_user $user_modify
                        if [ $? -eq 0 ]; then
                            echo $user_modify "changed to " $new_user
                        else
                            read -p "Press Enter to continue..."
                            continue
                        fi
                    else
                        echo "$user_modify not found!"
                    fi
                    ;;
                "cp")
                    read -p "which user? " name
                    if id "$name" > /dev/null 2>&1
                    then
                        sudo passwd "$name"
                    else
                        echo "$user_modify not found!"
                    fi

                    ;;
                *)
                    echo "Invalid choice."
                    ;;
            esac
            ;;



        ud)
            clear
            print_header
            echo "list of user:"
            getent passwd | cut -d: -f1,7 | grep -E '/bash$|/sh$' | sed '1,2d' | cut -d: -f1
            read -p "wich user do you want to delete: " delete_user
            sudo deluser --remove-home $delete_user
            ;;
        ga)
            clear
            print_header
            echo "Enter the group name"
            read -r group_name
            sudo groupadd "$group_name"
            echo "The group $group_name added successfully."
            ;;


        gl)
            clear
            print_header
            echo -e "\n*** List of System Groups ***"
            echo " "
            getent group | awk -F: '$3 >= 1000 {print $1}'
            echo " "

            ;;

        gv)
            clear
            print_header
            echo " "

            read -p "Enter the name of the group: " group_name

            # Check if the group exists
            if grep -q "^$group_name:" /etc/group; then
                # Get and display the users in the specified group
                group_members=$(getent group "$group_name" | cut -d: -f4)

                if [ -n "$group_members" ]; then
                    echo "Users in group '$group_name':"
                    for user in $group_members; do
                        echo "  - $user"
                    done
                else
                    echo "No users found in group '$group_name'."
                fi
            else
                echo "Error: Group '$group_name' not found."
            fi

            echo " "
            read -n 1 -s -r -p "Press any key to continue..."
            ;;
        gm)
            clear
            read -p "do you want add or remove a user a/r ?" answer
            answer=$(echo "$answer" | tr '[:upper:]' '[:lower:]')

            if [ $answer = "a" ]; then
                read -p "username: " user_name
                read -p "group's name: " group_name
                sudo usermod -a -G $group_name $user_name

                if [ $? -eq 0 ]; then
                    echo $user_name "added in " $group_name


                fi
            elif [ $answer = "r" ]; then
                read -p "username: " user_name
                read -p "group_name: " group_name
                sudo deluser $user_name $group_name

            else
                echo "command not found!"

            fi
            ;;
        gd)
            clear
            print_header
            echo "a list of all groups:"
            grep -A9999 'sambashare:x:136:' /etc/group | tail -n +2 | cut -d: -f1
            echo ""
            read -p "which group do you want to delete? " delete
            sudo groupdel $delete

            if [ $? -eq 0 ]; then
                echo $delete  " deleted"
            fi
            ;;
        fa)
            clear
            print_header
            echo "Enter the folder name: "
            read folder_name
            mkdir "$folder_name"
            echo "Folder '$folder_name' created successfully"
            ;;
        fl)
            # Implement Folder List
            echo "Folder List"
            # Add your folder list code here
            ;;
        fv)
            # Implement Folder View
            echo "Folder View"
            # Add your folder view code here
            ;;
        fm)
            # Implement Folder Modify
            echo "Folder Modify"
            # Add your folder modify code here
            ;;
        fd)
            clear
            print_header
            echo "list of folders:"
            ls -d */
            echo ""
            read -p "which folder" $folder
            rm -r $folder
            if [ $? -eq 0 ]; then
                echo $folder " deleted"
            fi
            ;;
        ex)
            # Exit the script
            echo "See you!"
            break
            ;;
        *)
            echo "Error: Invalid choice. Please try again."
            ;;
    esac

    read -p "Press Enter to continue..."
done

