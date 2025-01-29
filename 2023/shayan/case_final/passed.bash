#!/bin/bash

# Grupp 49
# David Khawari, Isak Nylander

CUR_PATH="/"

# main menu function (does not handle input)
print_main_menu () {
    clear

    SYSTEM_NAME="System Manager 1.0"
    SYSTEM_AUTH="David & Isak"
    PRE=$(($COLUMNS / 4 * 3))
    POST=$(($COLUMNS - $PRE - ${#SYSTEM_AUTH} - 2))

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    
    # put SYSTEM_NAME at halfway-mark
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#SYSTEM_NAME} / 2))))); do echo -n ' '; done
    echo -e "\e[41m$SYSTEM_NAME\e[0m"

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    
    # menus with formatting
    echo -e "\n"
    echo -e "    \e[91mf \e[0m- Folder Management\n"
    echo -e "    \e[91mg \e[0m- Group Management\n"
    echo -e "    \e[91mn \e[0m- Network Information\n"
    echo -e "    \e[91mu \e[0m- User Management\n"
    echo -e "    \e[91mx \e[0m- Exit\n"
    
    # fill ~70% of row with '-'
    for i in $(seq 1 $PRE); do echo -n '-'; done
    # append SYSTEM_AUTH to row
    echo -e -n " \e[41m$SYSTEM_AUTH\e[0m "
    # fill rest of row with '-'
    for i in $(seq 1 $POST); do echo -n '-'; done
    
    # user input ">> [input goes here]"
    echo -en "\n>> "
}


print_network_info() {
    echo " "
    echo "***Network Informations***"
    echo " "    
    echo "Computer Name:  $(hostname)"
    echo " "
    echo " "
    echo "Interface:      $(ip -o link show | grep -v "LOOPBACK" | awk '$2 !~ /lo/ {print $2}' | cut -d ":" -f 1)"
    echo "IP-Address:     $(hostname -I)"
    echo "Gateway:        $(ip route show default | awk '/default/ {print $3}')"
    echo "MAC-Address:    $(ip link | awk '/ether/ {print $2}')"
    echo "Status:         $(ip -o link show | awk '!/LOOPBACK/ {print $9}')"
    echo "------------------------------------------------------------------------------"
    echo " "
    read -n 1 -s -r -p "Press any key to continue..."
}

#all fuctions for group option

create_new_group() {
    echo -e "\n*** Create New Group ***"
    echo " "
    read -p "Enter the name of the new group: " new_group_name

    if grep -q "^$new_group_name:" /etc/group; then
        echo "Error: Group '$new_group_name' already exists."
    else
        sudo groupadd "$new_group_name"
        echo "Group '$new_group_name' created successfully."
    fi
    echo " "
    read -n 1 -s -r -p "Press any key to continue..."
}

list_system_groups() {
    echo -e "\n*** List of System Groups ***"
    echo " "
    getent group | awk -F: '$3 >= 1000 {print $1}'
    echo " "
    read -n 1 -s -r -p "Press any key to continue..."
}

add_user_to_group() {
    echo -e "\n*** Add User to a Group ***"
    echo " "
    read -p "Enter the name of the user: " username
    read -p "Enter the name of the group: " group_name

    # Check if the group exists
    if grep -q "^$group_name:" /etc/group; then
        # Check if the user is not already in the group
        if ! groups "$username" | grep -q "\<$group_name\>"; then
            # Check if the user exists
            if id "$username" &>/dev/null; then
                # Add the user to the group
                sudo usermod -aG "$group_name" "$username"
                echo "User '$username' added to group '$group_name' successfully."
            else
                # Create the user and add to the group
                if sudo useradd -m "$username"; then
                    sudo usermod -aG "$group_name" "$username"
                    echo "User '$username' created and added to group '$group_name' successfully."
                else
                    echo "Error: Failed to create user '$username'."
                fi
            fi
        else
            echo "Error: User '$username' is already a member of group '$group_name'."
        fi
    else
        echo "Error: Group '$group_name' not found."
    fi

    echo " "
    read -n 1 -s -r -p "Press any key to continue..."
}

list_users_in_specific_group() {
    echo -e "\n*** Show Users in Group ***"
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
}

remove_user_from_group_prompt() {
    echo -e "\n*** Remove User from a Group ***"
    echo " "
    read -p "Enter the name of the user: " username
    read -p "Enter the name of the group: " group_name

    if id "$username" &>/dev/null && grep -q "^$group_name:" /etc/group; then
        gpasswd -d "$username" "$group_name"
        echo "User '$username' removed from group '$group_name' successfully."
    else
        echo "Error: User '$username' or group '$group_name' not found."
    fi
    echo " "
    read -n 1 -s -r -p "Press any key to continue..."
}

delete_user_created_group() {
    echo -e "\n*** Delete User-Created Group ***"
    echo " "
    read -p "Enter the name of the group to delete: " group_name

    if grep -q "^$group_name:" /etc/group && [ -z "$(grep ":$group_name:" /etc/gshadow)" ]; then
        groupdel "$group_name"
        echo "Group '$group_name' deleted successfully."
    else
        echo "Error: Group '$group_name' not found or is a system group."
    fi
    echo " "
    read -n 1 -s -r -p "Press any key to continue..."
}

print_user_menu () {
    clear
    
    TITLE="User Management"

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[104m$TITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -e "\n"
    echo -e "    \e[94ma \e[0m- Add user\n"
    echo -e "    \e[94ml \e[0m- List users\n"
    echo -e "    \e[94mA \e[0m- Show attributes\n"
    echo -e "    \e[94me \e[0m- Edit attributes\n"
    echo -e "    \e[94mr \e[0m- Remove user\n" 
    echo -e "    \e[94mx \e[0m- Exit\n"

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -en "\n>> "
}

# user management / add user
user_management_add () {

    local usr
    local pwd

    local name_ready=false
    local pwd_ready=false

    # loop while username is empty or invalid
    while ! $name_ready; do
        clear
        echo -en "Please enter a \e[1musername\e[0m\n>> "
        read usr

        # username must match regex
        # (from unix.stackexchange)
        if [[ "$usr" =~ ^[a-z_]([a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\$)$ ]]; then
            name_ready=true
        fi
    done

    # loop while password is empty or invalid
    while ! $pwd_ready; do
        clear
        echo -e "Please enter a \e[1mpassword\e[0m"
        echo -n ">> "
        # -s, hide input
        read -s pwd

        # password must be of length > 7
        if [[ ${#pwd} -gt 7 ]]; then
            pwd_ready=true
        fi
    done

    # CREATE USER
    # -c, create with empty GECOS information (misc information)
    # -s, specify user default shell
    # -d, create user with specific home directory
    # -p, create password in /etc/shadow for user using openssl
    error=$(sudo useradd -c ",,," -s /bin/bash -m -d /home/$usr -p $(openssl passwd -1 "$pwd") "$usr" 2>&1)
    
    clear
    # make sure latest command (create user) ran without error
    if [[ $? -eq 0 ]]; then
        echo -e "Successfully added user \e[1m$usr\n\e[2m(Press enter to continue...)\e[0m"
        read confirm_exit
    else
        echo "There was an error: $error"
        echo -e "\e[2m(Press enter to continue...)\e[0m"
        read confirm_exit
    fi
}

# user management / list users
user_management_list () {
    # read /etc/passwd file
    # grep all lines NOT CONTAINING "nologin"
    # replace ":" with spaces
    # print users with a GID >= 1000 (man made users)
    clear
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    cat /etc/passwd | grep -v nologin | tr ':' ' ' | awk '{if ( $3 >= 1000  ) print $1}' | column
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

show_attributes () {
    clear

    NAME=$1
    PRE=$(($COLUMNS / 2 - $((${#NAME} / 2)) - 2))
    POST=$(($COLUMNS - $PRE - $((${#NAME} / 2)) - 6))

    for i in $(seq 1 $PRE); do echo -n '-'; done
    echo -en " \e[44m$NAME\e[0m "
    for i in $(seq 1 $POST); do echo -n '-'; done

    PASSWD_STRING=$(cat /etc/passwd | grep $NAME | tr ':' ' ')
    
    USERID=$(echo "$PASSWD_STRING" | awk '{print $3}') &> /dev/null
    PRIMARY_GID=$(echo "$PASSWD_STRING" | awk '{print $4}') &> /dev/null
    PRIMARY_GROUP=$(getent group "$PRIMARY_GID" | cut -d ':' -f 1) &> /dev/null
    GECOS=$(echo "$PASSWD_STRING" | awk '{print $5}') &> /dev/null
    HOMEDIR=$(echo "$PASSWD_STRING" | awk '{print $6}') &> /dev/null
    HOMESHELL=$(echo "$PASSWD_STRING" | awk '{print $7}') &> /dev/null

    echo -e "\n\e[1mUSERNAME\e[0m: $NAME"
    echo -e "\e[1mUSER ID\e[0m: $USERID"
    echo -e "\e[1mPRIMARY GROUP\e[0m: $PRIMARY_GROUP ($PRIMARY_GID)"
    echo -e "\e[2mALL GROUPS\e[0m: $(id $NAME | cut -d ' ' -f 3 | cut -b 8-)"
    echo -e "\e[1mGECOS\e[0m: $GECOS"
    echo -e "\e[1mHOME DIRECTORY\e[0m: $HOMEDIR"
    echo -e "\e[1mDEFAULT SHELL\e[0m: $HOMESHELL"

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -e "\n\n\e[2m(Press enter to exit...)\e[0m"
    read confirm_exit
}

# user management / show attributes
user_management_show () {
    local name

    clear
    echo -n "Show attributes for: "
    read name

    if id "$name" >/dev/null 2>&1
    then
        # user found
        show_attributes $name
    else 
        # user not found
        echo -e "The user \e[1m$name\e[0m was not found."
        echo -e "\e[2m(Press enter to continue...)\e[0m"
        read confirm_exit
    fi
}

# user management / edit attributes / change username
edit_username () {
    OLD=$1
    local NEW
    local name_ready=false

    while ! $name_ready; do
        clear
        echo -e "Enter new \e[1musername\e[0m for \e[1m$OLD\e[0m"
        echo -n ">> "
        read NEW

        # username is not in use && matches default rules
        # (regex once again from unix.stackexchange)
        if ! id "$NEW" &> /dev/null && [[ "$NEW" =~ ^[a-z_]([a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\$)$ ]];
        then
            name_ready=true
        fi
    done

    # change username
    # -l, specify new username
    sudo usermod -l $NEW $OLD &> /dev/null

    # i've also made sure that the underlying linux
    # core already takes care of things like:
    #   - reapply permissions for files
    #   - updates /etc/shadow file
    #   - migrates groups

    # DOES NOT HOWEVER, update home dir
    # below code handles that

    # update home dir name
    sudo mv /home/"$OLD" /home/"$NEW" &> /dev/null
    # assign new home dir to user
    sudo usermod -d /home/"$NEW" $NEW &> /dev/null

    echo -e "Successfully changed username of \e[1m\"$OLD\"\e[0m to \e[1m\"$NEW\"\e[0m"
    echo -e "\e[2m(Press enter to continue...)\e[0m"

    read confirm_exit
}

# user management / edit attributes / change password
edit_password () {
    NAME=$1
    local pwd
    local pwd_ready=false

    while ! $pwd_ready; do
        clear
        echo -e "Enter new \e[1mpassword\e[0m for \e[1m$NAME\e[0m"
        echo -n ">> "
        # -s, hide input
        read -s pwd

        # password must be of length greater than 7 (>= 8)
        if [[ ${#pwd} -gt 7 ]]; then
            pwd_ready=true
        fi
    done

    # chpasswd command takes a username:password pair
    # and updates /etc/shadow
    echo "$NAME:$pwd" | sudo chpasswd &> /dev/null

    echo -e "Successfully changed password of \e[1m\"$NAME\"\e[0m"
    echo -e "\e[2m(Press enter to continue...)\e[0m"

    read confirm_exit
}

# user management / edit attributes / change UID
edit_uid () {
    NAME=$1

    local uid
    local uid_ready=false

    while ! $uid_ready; do
        clear
        echo -e "Enter new \e[1mUID (User ID)\e[0m for \e[1m$NAME\e[0m"
        echo -n ">> "
        read uid

        # new uid must be >= 1000 (user reserved range)
        # & not already be in use
        if [[ $uid -ge 1000 ]] && [[ $(cat /etc/passwd | tr ':' ' ' | awk '{print $3}' | grep $uid | wc -c) -eq 0 ]]; then
            uid_ready=true
        fi
    done

    # change UID of $NAME
    sudo usermod -u $uid $NAME &> /dev/null

    echo -e "Successfully assigned \e[1mUID (User ID) $uid\e[0m to \e[1m$NAME\e[0m"
    echo -e "\e[2m(Press enter to continue...)\e[0m"

    read confirm_exit
}

# user management / edit attributes / change GID
edit_gid () {
    NAME=$1

    local gid
    local gid_ready=false

    while ! $gid_ready; do
        clear
        echo -e "Enter new \e[1mPrimary GID (Primary Group ID)\e[0m for \e[1m$NAME\e[0m"
        echo -n ">> "
        read gid

        # new gid must be valid (exist)
        if [[ $(getent group $gid | wc -l) -gt 0 ]]; then
            gid_ready=true
        fi
    done

    # assign new primary group
    # -a, keep other groups intact
    # -g, specify primary group
    sudo usermod -g $gid $name &> /dev/null

    echo -e "\e[1m$name\e[0m's new primary group is now \e[1m$(getent group $gid | cut -d: -f1)($gid)\e[0m"
    echo -e "\e[2m(Press enter to continue...)\e[0m"

    read confirm_exit
}

# user management / edit attributes / edit gecos
edit_gecos () {
    NAME=$1
    TITLE="Edit GECOS"

    local NEW

    clear

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[42m$TITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -e "\n"
    echo -e "    \e[32me \e[0m- Empty\n"
    echo -e "    \e[32ma \e[0m- Append\n"
    echo -e "    \e[32mx \e[0m- Exit\n"

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -en "\n>> "
    read choice

    case $choice in
        e) # write from empty
            clear
            echo -n "Content: "
            # -r, read whitespace (full string)
            read -r NEW
            # replace whitespace (' ') with underscore ('_')
            # sad necessity
            sudo usermod -c "$(echo $NEW | tr ' ' '_')" $NAME &> /dev/null
            echo -e "Successfully updated \e[1mGECOS\e[0m for \e[1m$NAME\e[0m"
            ;;
        a) # append
            local OLD=$(cat /etc/passwd | grep $NAME | cut -d : -f 5)
            clear
            echo -n "Content: "
            read -r NEW
            # append new content with ',' as delimiter
            sudo usermod -c "$OLD,$(echo $NEW | tr ' ' '_')" $NAME &> /dev/null
            echo -e "Successfully updated \e[1mGECOS\e[0m for \e[1m$NAME\e[0m"
            ;;
        x) # exit (do nothing)
            return
            ;;
        *) # unknown choice
            echo -e "Unknown choice \"$choice\""
            ;;
    esac

    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# user management / edit attributes / edit home directory
edit_home () {
    NAME=$1

    local new_home
    local home_ready=false

    while ! $home_ready; do
        echo -en "New \e[1mHome Directory Path\e[0m: "
        read new_home
        # $new_home must be directory
        # must not be another users home directory
        if [[ $(getent passwd | cut -d ':' -f 6 | grep $new_home | wc -l) -eq 0 ]]; then
            home_ready=true
        fi
        done

    # change home directory
    # -m, --move-home, moves content of
    #                  old home into new
    # -d, home directory flag
    sudo usermod -m -d $new_home $NAME

    echo -e "Successfully changed \e[1m$NAME\e[0m's \e[1mHome Directory \e[0mto \e[1m$new_home\e[0"
    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# user management / edit attributes / edit shell
edit_shell () {
    NAME=$1

    local new_shell
    local shell_ready=false

    while ! $shell_ready; do
        echo -en "New \e[1mDefault Shell Path\e[0m: "
        read new_shell

        # points to an executeable file
        # & is listed as a valid shell
        # in /etc/shells
        if [ -x $new_shell ] && grep -q "$new_shell" /etc/shells; then
            shell_ready=true
        fi
    done

    sudo usermod -s $new_shell $NAME

    echo -e "Successfully changed \e[1m$NAME\e[0m's \e[1mDefault Shell\e[0m to \e[1m$new_shell\e[0m"
    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# user management / edit attributes
user_management_edit () {
    local name

    clear
    echo -n "Edit attributes for: "
    read name

    if id "$name" >/dev/null 2>&1
    then
        # user found
        local choice
        clear
        for i in $(seq 1 $COLUMNS); do echo -n '-'; done
        echo -e "\n"
        echo -e "    \e[36mu \e[0m- Username\n"
        echo -e "    \e[36mp \e[0m- Password\n"
        echo -e "    \e[36mUID \e[0m- User ID\n"
        echo -e "    \e[36mGID \e[0m- Group ID (Primary)\n"
        echo -e "    \e[36mg \e[0m- GECOS\n"
        echo -e "    \e[36mh \e[0m- Home Directory\n"
        echo -e "    \e[36ms \e[0m- Default Shell\n"
        echo -e "    \e[36mx \e[0m- Exit\n"
        for i in $(seq 1 $COLUMNS); do echo -n '-'; done
        echo -en "\n>> "
        read choice
        case $choice in
            u) # username
                edit_username $name
                ;;
            p) # password
                edit_password $name
                ;;
            UID | uid) # UID
                edit_uid $name
                ;;
            GID | gid) # (Primary) GID
                edit_gid $name
                ;;
            g) # GECOS
                edit_gecos $name
                ;;
            h) # home directory
                edit_home $name
                ;;
            s) # default shell
                edit_shell $name
                ;;
            x) # exit (do nothing)
                return
                ;;
            *) # unknown choice
                echo -e "Unknown attribute \"$choice\"\n\e[2m(Press enter to exit...)\e[0m"
                read confirm_exit
                ;;
        esac
    else
        # user not found
        echo -e "The user \e[1m$name\e[0m was not found."
        echo -e "\e[2m(Press enter to continue...)\e[0m"
        read confirm_exit
    fi
}

#user management / remove
user_management_remove () {
    local name
    clear
    echo -en "User to be \e[41mRemoved\e[0m: "
    read name
    # getent passwd = cat /etc/passwd
    if getent passwd | cut -d ':' -f 1 | grep $name &> /dev/null; then
        echo -e "Are you sure you want to \e[41mPermanently Remove \e[1m$name\e[0m? (y/n)" 
        read choice
        case $choice in
            y | Y)
                # kill all processes using USER
                sudo killall -u $name &> /dev/null
                # remove user
                # -r, remove home dir and containing files
                sudo userdel -r $name &> /dev/null
                clear
                echo -e "User \e[1m$name\e[0m has been successfully removed."
                ;;
            *)
                return
                ;;
        esac
    else
        echo -e "User \e[1m\"$name\"\e[0m not found."
    fi

    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# user management
user_management_menu () {
    quit=false
    while ! quit; do
        
        print_user_menu
        read menu_flag
    
        if [[ ${#menu_flag} == 1 ]]; then

            case $menu_flag in

                a) # add user
                    user_management_add
                    ;;

                l) # list users
                    user_management_list
                    ;;

                A) # show attributes
                    user_management_show
                    ;;

                e) # edit attributes
                    user_management_edit
                    ;;

                r) # remove user
                    user_management_remove
                    ;;

                x) # exit
                    quit=true
                    break;

            esac
        fi
    done
}

print_folder_menu () {
    clear

    TITLE="Folder Management"

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[104m$TITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -e "\n"
    echo -e "    \e[94mt \e[0m- Traverse (Relative)\n"
    echo -e "    \e[94mc \e[0m- Create Folder\n"
    echo -e "    \e[94ml \e[0m- List Content\n"
    echo -e "    \e[94ma \e[0m- Show Attributes\n"
    echo -e "    \e[94me \e[0m- Edit Attributes\n"
    echo -e "    \e[94mr \e[0m- Remove Folder\n"
    echo -e "    \e[94mx \e[0m- Exit\n"

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -en "\n>> "
}

# folder management / traverse
traverse () {
    TITLE="Directories in current path:"
    SUBTITLE=$CUR_PATH
    
    clear
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[104m$TITLE\e[0m"
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#SUBTITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[34m$SUBTITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done 
    
    # '^d', regex, grep where permission string begins
    # with an 'd' (i.e. directories only)
    # tr -s, squish following spaces into only 1
    # column -x, fill row before column
    ls -l $CUR_PATH | grep '^d' | tr -s ' ' | cut -d ' ' -f 9 | column -x
    
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -en "\n>> "

    read traversal

    # exit condition
    if [ $traversal == 'x' ]; then
        return
    else
        # validate users given path
        # (test -d [path])
        if [ -d $CUR_PATH/$traversal ]; then
            # check for backwards traversal
            if [ $traversal == ".." ]; then
                # trim last backslash '/'
                CUR_PATH=$(dirname "$CUR_PATH")
            else
                CUR_PATH="$CUR_PATH/$traversal"
            fi
            # continue traversal at new path
            traverse
        else
            echo -e "Unknown directory \"$CUR_PATH/$traversal\"\n\e[2m(Press enter to continue...)\e[0m"
            read confirm_exit
        fi
    fi
}

# folder management / create folder
create_folder () {
    TITLE="Create new Folder"
    SUBTITLE="NOTE: Creating at current path: $CUR_PATH"

    clear

    # header
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[42m$TITLE\e[0m"
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#SUBTITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[32m$SUBTITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -n "Folder name: "

    read folder_name

    # check if folder already exists
    if [ -d "$CUR_PATH/$folder_name" ]; then
        echo -e "Folder already exists! \e[2m($CUR_PATH/$folder_name)\e[0m"
    else
        # if folder does not exist, create it
        sudo mkdir "$CUR_PATH/$folder_name"
    fi

    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# folder management / list content
list_content () {
    TITLE="$CUR_PATH"

    clear

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[45m$TITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    ls -l "$CUR_PATH" | grep '^d' | tr -s ' ' | cut -d ' ' -f 9 | column -x

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -e "\n\e[2m(Press enter to continue)"
    read confirm_exit
}

# folder management / show attributes
show_folder_attributes () {
    clear

    TITLE="$CUR_PATH's Attributes"
    STRING=$(ls -la "$CUR_PATH" | sed -n '2p' | tr -s ' ')

    OWNER=$(echo "$STRING" | cut -d ' ' -f 3 | tr -s ' ')
    GROUP=$(echo "$STRING" | cut -d ' ' -f 4 | tr -s ' ')

    # permission related

    OWN_PERM=$(echo "$STRING" | cut -b 2-4 | tr -s ' ')
    GRP_PERM=$(echo "$STRING" | cut -b 5-7 | tr -s ' ')
    OTH_PERM=$(echo "$STRING" | cut -b 8-10 | tr -s ' ')

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[41m$TITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -e "\e[1mOwner\e[0m: $OWNER"
    echo -e "\e[1mGroup\e[0m: $GROUP\n"

    echo -e "\e[2mAdvanced permission string: ($(echo "$STRING" | cut -d ' ' -f 1))\e[0m"

    #   owner related permissions
    
    # read
    if [[ $(echo $OWN_PERM | cut -b 1) == '-' ]]; then
        echo -e "\e[1mOwner reading \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "\e[1mOwner reading \e[0mpermission: \e[32mYES\e[0m"
    fi
    
    # write
    if [[ $(echo $OWN_PERM | cut -b 2) == '-' ]]; then 
        echo -e "\e[1mOwner writing \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "\e[1mOwner writing \e[0mpermission: \e[32mYES\e[0m"
    fi

    # execute
    if [[ $(echo $OWN_PERM | cut -b 3) == '-' ]]; then
        echo -e "\e[1mOwner execute \e[0mpermission: \e[31mNO\e[0m\n"
    else
        echo -e "\e[1mOwner execute \e[0mpermission: \e[32mYES\e[0m\n"
    fi

    #   group related permissions

    # read
    if [[ $(echo $GRP_PERM | cut -b 1) == '-' ]]; then
        echo -e "\e[1mGroup reading \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "\e[1mGroup reading \e[0mpermission: \e[32mYES\e[0m"
    fi

    # write
    if [[ $(echo $GRP_PERM | cut -b 2) == '-' ]]; then
        echo -e "\e[1mGroup writing \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "\e[1mGroup writing \e[0mpermission: \e[32mYES\e[0m"
    fi

    # execute
    if [[ $(echo $GRP_PERM | cut -b 3) == '-' ]]; then
        echo -e "\e[1mGroup execute \e[ompermission: \e[31mNO\e[0m\n"
    elif [[ $(echo $GRP_PERM | cut -b 3) == 's' ]]; then
        echo -e "\e[1mDirectory \e[0mhas \e[1msetgid \e[32mactivated \e[0mwith execute permissions\n"
    elif [[ $(echo $GRP_PERM | cut -b 3) == 'S' ]]; then
        echo -e "\e[1mDirectory \e[0mhas \e[1msetgid \e[32mactivated \e[31mwithout \e[0mexecute permissions\n"
    else
        echo -e "\e[1mGroup execute \e[0mpermission: \e[32mYES\e[0m\n"
    fi

    #   other related permissions

    # read
    if [[ $(echo $OTH_PERM | cut -b 1) == '-' ]]; then
        echo -e "\e[1mOther reading \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "\e[1mOther reading \e[0mpermission: \e[32mYES\e[0m"
    fi

    # write
    if [[ $(echo $OTH_PERM | cut -b 2) == '-' ]]; then
        echo -e "\e[1mOther writing \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "\e[1mOther writing \e[0mpermission: \e[32mYES\e[0m"
    fi

    # execute
    if [[ $(echo $OTH_PERM | cut -b 3) == '-' ]]; then
        echo -e "\e[1mOther execute \e[0mpermission: \e[31mNO\e[0m\n"
    elif [[ $(echo $OTH_PERM | cut -b 3) == 't' ]]; then
        echo -e "\e[1mDirectory \e[0mhas \e[1msticky bit \e[32mactivated \e[0mwith permission set\n"
    elif [[ $(echo $OTH_PERM | cut -b 3) == 'T' ]]; then
        echo -e "\e[1mDirectory \e[0mhas \e[1msticky bit \e[32mactivated \e[31mwithout \e[0mpermission set\n"
    else
        echo -e "\e[1mOther execute \e[0mpermission: \e[32mYES\e[0m\n"
    fi


    # last modified

    echo -e "\e[1mLast modified\e[0m: $(echo "$STRING" | awk '{print $7 " " $6 " at " $8}')\n"

    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# folder management / edit attributes
edit_folder_attributes () {
    TITLE="Edit $CUR_PATH's Attributes"

    clear

    for i in $(seq 1 $COLUMNS); do echo -n '-'; done
    for i in $(seq 1 $(($COLUMNS / 2 - $((${#TITLE} / 2))))); do echo -n ' '; done
    echo -e "\e[42m$TITLE\e[0m"
    for i in $(seq 1 $COLUMNS); do echo -n '-'; done

    echo -e "\n"
    echo -e "    \e[34mo  \e[0m- Change Owner"
    echo -e "    \e[34mg  \e[0m- Change Group\n"
    echo -e "    \e[34mr1 \e[0m- Toggle Owner Read Permission"
    echo -e "    \e[34mw1 \e[0m- Toggle Owner Write Permission"
    echo -e "    \e[34mx1 \e[0m- Toggle Owner Execute Permission\n"
    echo -e "    \e[34mr2 \e[0m- Toggle Group Read Permission"
    echo -e "    \e[34mw2 \e[0m- Toggle Group Write Permission"
    echo -e "    \e[34mx2 \e[0m- Toggle Group Execute Permission\n"
    echo -e "    \e[34mr3 \e[0m- Toggle Other Read Permission"
    echo -e "    \e[34mw3 \e[0m- Toggle Other Write Permission"
    echo -e "    \e[34mx3 \e[0m- Toggle Other Execute Permission\n"
    echo -e "    \e[34mG  \e[0m- Toggle SetGID"
    echo -e "    \e[34mT  \e[0m- Toggle Sticky Bit\n"
    echo -e "    \e[34mn  \e[0m- Change Name"

    echo -en "\n>> "

    read choice

    # stat -c "%A" $CUR_PATH, grabs only the permission string
    # from specified directory
    # then cut / grab only necessary bit
    # touch $CUR_PATH updates "Last Modified"
    case $choice in
        o)
            clear
            echo -en "Enter new owner: "
            read new_owner
            if getent passwd $new_owner &> /dev/null; then
                # command subsitution grabs the current group of dir
                sudo chown $new_owner:$(stat -c "%G" $CUR_PATH) $CUR_PATH
                touch $CUR_PATH
            else
                echo -e "No user by the name of \"$new_owner\""
            fi
            ;;
        g)
            clear
            echo -en "Enter new group: "
            read new_group
            if getent group $new_group &> /dev/null; then
                # command subsitution grabs the current owner of dir
                sudo chown $(stat -c "%U" $CUR_PATH):$new_group $CUR_PATH
                touch $CUR_PATH
            else
                echo -e "No group by the name or GID of \"$new_group\""
            fi
            ;;
        r1)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 2) == '-' ]; then
                sudo chmod u+r $CUR_PATH
            else
                sudo chmod u-r $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        w1)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 3) == '-' ]; then
                sudo chmod u+w $CUR_PATH
            else
                sudo chmod u-w $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        x1)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 4) == '-' ]; then
                sudo chmod u+x $CUR_PATH
            else
                sudo chmod u-x $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        r2)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 5) == '-' ]; then
                sudo chmod g+r $CUR_PATH
            else
                sudo chmod g-r $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        w2)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 6) == '-' ]; then
                sudo chmod g+w $CUR_PATH
            else
                sudo chmod g-w $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        x2)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 7) == '-' ] || [ $(stat -c "%A" $CUR_PATH | cut -b 7) == 'S' ]; then
                sudo chmod g+x $CUR_PATH
            else
                sudo chmod g-x $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        r3)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 8) == '-' ]; then
                sudo chmod o+r $CUR_PATH
            else
                sudo chmod o-r $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        w3)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 9) == '-' ]; then
                sudo chmod o+w $CUR_PATH
            else
                sudo chmod o-w $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        x3)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 10) == '-' ] || [ $(stat -c "%A" $CUR_PATH | cut -b 10) == 'T' ]; then
                sudo chmod o+x $CUR_PATH
            else
                sudo chmod o-x $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        G)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 7) == 's' ] || [ $(stat -c "%A" $CUR_PATH | cut -b 7) == 'S' ]; then
                sudo chmod g-s $CUR_PATH
            else
                sudo chmod g+s $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        T)
            if [ $(stat -c "%A" $CUR_PATH | cut -b 10) == 't' ] || [ $(stat -c "%A" $CUR_PATH | cut -b 10) == 'T' ]; then
                sudo chmod o-t $CUR_PATH
            else
                sudo chmod o+t $CUR_PATH
            fi
            touch $CUR_PATH
            ;;
        n)
            clear
            echo -n "Enter new name for directory: "
            read new_name
            # check if folder already exists
            if [ -d "$(dirname "$CUR_PATH")/$new_name" ] &> /dev/null; then
                echo -e "Directory \"$new_name\" already exists"
            else
                # if not, rename and update $CUR_PATH
                sudo mv "$CUR_PATH" "$(dirname "$CUR_PATH")/$new_name"
                CUR_PATH="$(dirname "$CUR_PATH")/$new_name"
                touch $CUR_PATH
            fi
            ;;
        *)
            echo -e "Unknown choice \"$choice\""
            ;;
    esac

    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# folder management / remove folder
remove_folder () {
    TITLE="Removal of $CUR_PATH"

    clear

    echo -en "You are about to \e[31mPermanently remove $CUR_PATH\n\e[0m(y/n) "
    read removal_confirmation

    case $removal_confirmation in
        y | Y)
            sudo rm -r $CUR_PATH
            echo -e "Successfully removed $CUR_PATH"
            CUR_PATH="$(dirname "$CUR_PATH")"
            ;;
        n | N)
            return
            ;;
        *)
            echo -e "Unknown choice \"$removal_confirmation\""
            ;;
    esac

    echo -e "\e[2m(Press enter to continue...)\e[0m"
    read confirm_exit
}

# folder management
folder_management_menu () {
    quit=false
    while ! quit; do

        print_folder_menu
        read menu_flag

        if [[ ${#menu_flag} == 1 ]]; then

            case $menu_flag in

                t) # traverse (relative path)
                    traverse
                    ;;

                c) # create folder
                    create_folder
                    ;;

                l) # list content
                    list_content
                    ;;

                a) # show attributes
                    show_folder_attributes
                    ;;

                e) # edit attributes
                    edit_folder_attributes
                    ;;

                r) # remove folder
                    remove_folder
                    ;;

                x) # exit
                    quit=true
                    break;
                    ;;

                *) # unknown flag
                    echo -e "Unknown flag \"$menu_flag\"\n\e[2m(Press enter to continue...)\e[0m"
                    read confirm_exit
                    ;;

            esac
        fi
    done
}

# assert we are running script with root priviligies
if [[ $UID != 0 ]]; then
    echo "No root priviligies found, exiting."
    echo -e "Run \"sudo !!\" to execute as root"

else
    # assuming infinite-loops are OK since there is a
    # clear stop condition in the menu
    while true; do
        
        print_main_menu
        read menu_flag
        
        # assert user input is only 1 character
        # (might be needed for quick commands)
        if [[ ${#menu_flag} == 1 ]]; then

            case $menu_flag in

                f) # Folder management (Isak)
                    folder_management_menu
                    ;;

                g)
                    #sub-menu for group management (David)
                    while true; do
                        clear
                        echo " "
  			echo " "
                        echo -e "    \e[91]1 \e[0m- Create New Group\n"
                        echo -e "    \e[91]2 \e[0m- List System Groups\n"
                        echo -e "    \e[91]3 \e[0m- List Users in a Specific Group\n"
                        echo -e "    \e[91]4 \e[0m- Add User to a Group\n"
                        echo -e "    \e[91]5 \e[0m- Remove User from a Group\n"
                        echo -e "    \e[91]6 \e[0m- Delete User-Created Group\n"
                        echo -e "    \e[91]b \e[0m- Go Back\n"
			echo "::::::::::::::::::::::::::::::::::::::"
                        echo -e -n "\nEnter the command nummber: "
                        read group_option

                        case $group_option in
                            1)
                                create_new_group
                                ;;
                            2)
                                list_system_groups
                                ;;
                            3)
                                list_users_in_specific_group
                                ;;
                            4)
                                add_user_to_group
                                ;;
                            5)
                                remove_user_from_group_prompt
                                ;;
                            6)
                                delete_user_created_group
                                ;;
                            b)
                                break
                                ;;
                            *)
                                echo "Invalid option. Try again."                         
			       	;;
                         esac
                    done
                    ;;
 
                n) # Network info (David)
                    print_network_info
                    ;;

                u) # User Management (Isak)
                    user_management_menu
                    ;;

                x)
                    exit
                    ;;

                *)
                    echo "???"
                    ;;
            esac
        # else: user input length > 1
        else
            # handle colon(:) quick commands
            echo "quick command"
        fi
    done
fi

