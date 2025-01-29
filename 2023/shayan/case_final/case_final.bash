#! /bin/bash

# TODO:
# -----------
# [done]  ni
# [done]  ua
# [done]  ul
# [done]  uv
# [done]  um
# [todo]  ud
#
# [done]  ga
# [done]  gl
# [done]  gv
# [done]  gm
# [done]  gd
#
# [done]  fa
# [done]  fl
# [done]  fv
# [todo]  fm
# [todo]  fd
#
# [done]  ex



RED='\033[0;31m'
WHITE='\e[1m'
GREEN='\033[32m'
BOLD='\033[1m'
RESET='\033[0m'
CUR_PATH="/"

# Check if the user is root
# Every user has a id number
# the root user has the id 0
# if id of the user is not 0
# the message will `This script must be run  as root` will print.
# and rest of the file will be ignored (exit 1)
if [[ $(id -u) -ne 0 ]]; then
    echo "This script must be run as root"
    exit 1
fi

# seq print series of number form start to stop;  similer to python `range` function.
# $COLUMN is a enviroment variable which store terminal's width.
# `-n` in `echo` will prevent print a newline a the end of the text
function print_dashed_line() {
    for i in $(seq 1 $COLUMNS)
    do
        echo -n '-'
    done
}

# This function print TEXT in the CENTER Of the terminal.
# TEXT is the text of the message
# TEXT is the first argument of the function.
# #TEXT returns length of the TEXT j
# tput returns terminal information which in this case we get the width of the terminal
# usin `cols`  argument.
function print_message() {
    local TEXT="$1"
    local COLS
    COLS=$(tput cols)
    local SPACES=$(( (COLS - ${#TEXT}) / 2 ))
    printf "%*s" $SPACES
    echo "$TEXT"
}

# print information about the app
function print_header() {
    print_dashed_line
    print_message "MANAGER (version 1.0.0)"
    print_dashed_line
}

# Print main menu.
function print_menu() {
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
    print_dashed_line
}

# ----------------
# NETWORK
# ----------------

# Print network information.
function net_info() {
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
}

# ----------------------
#     USER MAGEMENT
# ----------------------
# Get a username and check it existence
# if user exist return 0 meaning False
function is_user_exist() {
    username="$1"
    # Check if the user already exists
    if id "$username" &>/dev/null; then
        return 0
    else
        return 1
    fi
}

function user_add() {
    # Prompt for username
    read -rp "Enter the username: " username
    # check if user exist or not.
    if is_user_exist "$username"; then
        echo -e "${RED}User already exist.${RESET}"
        return
    fi

    # prompt password
    read -rsp "Enter the password: " password
    echo ""
    read -rsp "Repeat the password: " repeat_password
    echo ""
    # Check if passwords match
    if [ "$password" != "$repeat_password" ]; then
        echo -e "${RED}Passwords do not match.${RESET} "
        return
    fi

    # Create the user with the provided credentials
    RESULT=$(sudo useradd -m -p "$(openssl passwd -1 "$password")" "$username")

    # Check if user creation was successful
    if $RESULT; then
        echo -e  "${GREEN}User '$username' created successfully.${RESET}"
    else
        echo -e "Failed to create user '$username'."
    fi
}


function user_list() {
    grep -v nologin /etc/passwd | tr ':' ' ' | awk '{if ( $3 >= 1000  ) print $1}' | column
}


function user_view() {
    read -rp "enter username to view: " user
    passwd_line=$(grep "$user" /etc/passwd)
    # Check if user not exist
    if ! is_user_exist "$user" &>/dev/null; then
        echo -e "${RED}ERROR: No such a user ${BOLD}$user${RESET}"
        return
    fi

    # extract the data from passwd_line based on `:` character.
    IFS=':' read -r username password uid gid fullname home shell <<< "$passwd_line"
    echo -e "Properties for user: ${BOLD}$user${RESET}"
    echo ""
    echo -e "${RED}User:${RESET}          $username"
    echo -e "${RED}Password:${RESET}      $password"
    echo -e "${RED}User-ID:${RESET}       $uid"
    echo -e "${RED}Group-ID:${RESET}      $gid"
    echo -e "${RED}Comment:${RESET}       $fullname"
    echo -e "${RED}Directory:${RESET}     $home"
    echo -e "${RED}Shell:${RESET}         $shell"
    echo ""
    echo -e "${RED}Groups:${RESET}        $(id -nG "$user" | tr ' ' ',')"
}


function user_modify_menu() {
    echo -e "${RED}sa${RESET} - Show attributes"
    echo -e "${RED}ea${RESET} - Edit attributes"
    echo -e "${RED}cu${RESET} - Change username"
    echo -e "${RED}cp${RESET} - Change password"
    echo -e "${RED}ex${RESET} - Back to main menu"
    echo ""
}

function user_show_attr() {
    clear
    read -rp "Show attributes for: " name
    # ????
    if id "$name" >/dev/null 2>&1
    then
        PASSWD_STRING=$(grep "^$name:" /etc/passwd)
        USERID=$(echo "$PASSWD_STRING" | cut -d: -f3)
        PRIMARY_GID=$(echo "$PASSWD_STRING" | cut -d: -f4)
        PRIMARY_GROUP=$(getent group "$PRIMARY_GID" | cut -d: -f1)
        GECOS=$(echo "$PASSWD_STRING" | cut -d: -f5)
        HOMEDIR=$(echo "$PASSWD_STRING" | cut -d: -f6)
        HOMESHELL=$(echo "$PASSWD_STRING" | cut -d: -f7)

        echo -e "\n${WHITE}USERNAMEi${RESET}: $name"
        echo -e "${WHITE}USER ID${RESET}: $USERID"
        echo -e "${WHITE}PRIMARY GROUP${RESET}: $PRIMARY_GROUP ($PRIMARY_GID)"
        echo -e "${WHITE}ALL GROUPS${RESET}: $(id "$name" | cut -d' ' -f3 | cut -b 8-)"
        echo -e "${WHITE}GECOS${RESET}: $GECOS"
        echo -e "${WHITE}HOME DIRECTORY${RESET}: $HOMEDIR"
        echo -e "${WHITE}DEFAULT SHELL${RESET}: $HOMESHELL"
    else
        echo "User $name not found."
    fi
}



function user_edit_attr() {
    echo -e "${RED}1${RESET} - Change GECOS (comment)"
    echo -e "${RED}2${RESET} - Change Home Directory"
    echo -e "${RED}3${RESET} - user id (comment)"
    echo -e "${RED}4${RESET} - group id (comment)"
    echo -e "${RED}5${RESET} - default shell (comment)"
    echo -e "${RED}0${RESET} - Back to main menu"

    read -rp "Enter option: " edit_option
    read -rp "user: " name
    case $edit_option in
        1)
            read -rp "Enter new GECOS: " new_gecos
            sudo usermod -c "$new_gecos" "$name"
            if [ $? -eq 0 ]; then
                echo "GECOS changed to: $new_gecos"
            else
                echo "Failed to change GECOS."
            fi
            ;;
        2)
            read -rp "Enter new home directory: " new_homedir
            sudo usermod -d "$new_homedir" -m "$name"
            if [ $? -eq 0 ]; then
                echo "Home directory changed to: $new_homedir"
            else
                echo "Failed to change home directory."
            fi
            ;;
        3)
            read -rp "Enter new User ID: " new_uid
            if id -u "$new_uid" &>/dev/null; then
                echo "it's already used $new_uid"

            elif [ "$new_uid" -le 1000 ]; then
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
            read -rp "Enter new Group ID: " new_gid
            sudo usermod -g "$new_gid" "$name"
            if [ $? -eq 0 ]; then
                echo "Group ID changed to: $new_gid"
            else
                echo "Failed to change Group ID."
            fi
            ;;
        5)
            read -rp "Enter new Default Shell: " new_shell
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
}

function user_change_username() {
    read -rp "which username: " user_modify
    if id "$user_modify" > /dev/null 2>&1
    then
        read -rp "write the new username: " new_user
        sudo usermod -l "$new_user" "$user_modify"
        if [ $? -eq 0 ]; then
            echo "$user_modify" "changed to " "$new_user"
        else
            read -rp "Press Enter to continue..."
            return
        fi
    else
        echo "$user_modify not found!"
    fi
}

function user_change_password() {
    read -rp "which user? " name
    if id "$name" > /dev/null 2>&1
    then
        sudo passwd "$name"
    else
        echo "$user_modify not found!"
    fi
}

function user_delete() {
    local name
    echo -en "User to be Removed: "
    read -r name
    # getent passwd = cat /etc/passwd
    if getent passwd | cut -d ':' -f 1 | grep "$name" &> /dev/null; then
        echo -en "Are you sure you want to ${RED}${BOLD}Permanently Remove $name?${RESET} (y/n) "
        read -r choice
        case $choice in
            y | Y)
                # kill all processes using USER
                sudo killall -u "$name" &> /dev/null
                # remove user
                # -r, remove home dir and containing files
                sudo userdel -r "$name" &> /dev/null
                echo -e "${GREEN}User ${BOLD}$name${RESET} has been successfully removed.${RESET}"
                ;;
            *)
                return
                ;;
        esac
    else
        echo -e "${RED}User $name not found.${RESET}"
    fi
}

#----------------------------
#   GROUP MANAGEMENT
#----------------------------
function group_add() {
    echo -n "Enter the group name: "
    read -r new_group_name

    if grep -q "^$new_group_name:" /etc/group; then
        echo -e "${RED}Error: Group '$new_group_name' already exists.${RESET}"
    else
        sudo groupadd "$new_group_name"
        echo -e "${GREEN}Group '$new_group_name' created successfully.${RESET}"
    fi
}

# getent: show all groups in column fromat that each field sperated with `:`
# if 3 column value greather that 1000 it is a group
# group name is in the first column `print $1`
function group_list() {
    echo -e "\n*** List of System Groups ***"
    getent group | awk -F: '$3 >= 1000 {print $1}'
}

function group_view() {
    read -rp "Enter the name of the group: " group_name

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
            echo -e "${RED}No users found in group '$group_name'.${RESET}"
        fi
    else
        echo -e "${RED}Error: Group '$group_name' not found.${RESET}"
    fi

}

function group_modify() {

    read -rp "do you want add or remove a user a/r ?" answer
    answer=$(echo "$answer" | tr '[:upper:]' '[:lower:]')

    if [ "$answer" = "a" ]; then
        read -rp "username: " user_name
        read -rp "group's name: " group_name
        sudo usermod -a -G "$group_name" "$user_name"

        if [ $? -eq 0 ]; then
            echo "$user_name" "added in " "$group_name"
        fi
    elif [ "$answer" = "r" ]; then
        read -rp "username: " user_name
        read -rp "group_name: " group_name
        sudo deluser "$user_name" "$group_name"
    else
        echo "command not found!"
    fi
}

function group_delete() {
    echo "a list of all groups:"
    group_list
    read -rp "which group do you want to delete? " delete
    sudo groupdel "$delete"

    if [ $? -eq 0 ]; then
        echo -e  "${GREEN}$delete"  " deleted${RESET}"
    fi
}


# -------------------
# FOLDER MANAGEMENT
# -------------------
function folder_add () {
    echo -n "Folder name: "
    read -r folder_name

    # check if folder already exists
    if [ -d "$CUR_PATH/$folder_name" ]; then
        echo -e "${RED}Folder already exists! \e[2m($CUR_PATH/$folder_name)${RESET}"
    else
        # if folder does not exist, create it
        sudo mkdir "$CUR_PATH/$folder_name"
        echo -e "${GREEN}Folder Created Sunccessfuly.${RESET}"
    fi
}


function folder_list () {
    ls -l "$CUR_PATH" | grep '^d' | tr -s ' ' | cut -d ' ' -f 9 | column -x
}

function folder_view () {
    clear

    TITLE="$CUR_PATH's Attributes"
    STRING=$(ls -la "$CUR_PATH" | sed -n '2p' | tr -s ' ')

    OWNER=$(echo "$STRING" | cut -d ' ' -f 3 | tr -s ' ')
    GROUP=$(echo "$STRING" | cut -d ' ' -f 4 | tr -s ' ')

    # permission related

    OWN_PERM=$(echo "$STRING" | cut -b 2-4 | tr -s ' ')
    GRP_PERM=$(echo "$STRING" | cut -b 5-7 | tr -s ' ')
    OTH_PERM=$(echo "$STRING" | cut -b 8-10 | tr -s ' ')


    echo -e "${WHITE}Owner\e[0m: $OWNER"
    echo -e "${WHITE}Group\e[0m: $GROUP\n"

    echo -e "\e[2mAdvanced permission string: ($(echo "$STRING" | cut -d ' ' -f 1))\e[0m"

    #   owner related permissions

    # read
    if [[ $(echo $OWN_PERM | cut -b 1) == '-' ]]; then
        echo -e "${WHITE}Owner reading \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "${WHITE}Owner reading \e[0mpermission: \e[32mYES\e[0m"
    fi

    # write
    if [[ $(echo "$OWN_PERM" | cut -b 2) == '-' ]]; then
        echo -e "${WHITE}Owner writing \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "${WHITE}Owner writing \e[0mpermission: \e[32mYES\e[0m"
    fi

    # execute
    if [[ $(echo "$OWN_PERM" | cut -b 3) == '-' ]]; then
        echo -e "${WHITE}Owner execute \e[0mpermission: \e[31mNO\e[0m\n"
    else
        echo -e "${WHITE}Owner execute \e[0mpermission: \e[32mYES\e[0m\n"
    fi

    #   group related permissions

    # read
    if [[ $(echo "$GRP_PERM" | cut -b 1) == '-' ]]; then
        echo -e "${WHITE}Group reading \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "${WHITE}Group reading \e[0mpermission: \e[32mYES\e[0m"
    fi

    # write
    if [[ $(echo "$GRP_PERM" | cut -b 2) == '-' ]]; then
        echo -e "${WHITE}Group writing \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "${WHITE}Group writing \e[0mpermission: \e[32mYES\e[0m"
    fi

    # execute
    if [[ $(echo "$GRP_PERM" | cut -b 3) == '-' ]]; then
        echo -e "${WHITE}Group execute \e[ompermission: \e[31mNO\e[0m\n"
    elif [[ $(echo "$GRP_PERM" | cut -b 3) == 's' ]]; then
        echo -e "${WHITE}Directory \e[0mhas ${WHITE}setgid \e[32mactivated \e[0mwith execute permissions\n"
    elif [[ $(echo "$GRP_PERM" | cut -b 3) == 'S' ]]; then
        echo -e "${WHITE}Directory \e[0mhas ${WHITE}setgid \e[32mactivated \e[31mwithout \e[0mexecute permissions\n"
    else
        echo -e "${WHITE}Group execute \e[0mpermission: \e[32mYES\e[0m\n"
    fi

    #   other related permissions

    # read
    if [[ $(echo "$OTH_PERM" | cut -b 1) == '-' ]]; then
        echo -e "${WHITE}Other reading \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "${WHITE}Other reading \e[0mpermission: \e[32mYES\e[0m"
    fi

    # write
    if [[ $(echo "$OTH_PERM" | cut -b 2) == '-' ]]; then
        echo -e "${WHITE}Other writing \e[0mpermission: \e[31mNO\e[0m"
    else
        echo -e "${WHITE}Other writing \e[0mpermission: \e[32mYES\e[0m"
    fi

    # execute
    if [[ $(echo "$OTH_PERM" | cut -b 3) == '-' ]]; then
        echo -e "${WHITE}Other execute \e[0mpermission: \e[31mNO\e[0m\n"
    elif [[ $(echo "$OTH_PERM" | cut -b 3) == 't' ]]; then
        echo -e "${WHITE}Directory \e[0mhas ${WHITE}sticky bit \e[32mactivated \e[0mwith permission set\n"
    elif [[ $(echo "$OTH_PERM" | cut -b 3) == 'T' ]]; then
        echo -e "${WHITE}Directory \e[0mhas ${WHITE}sticky bit \e[32mactivated \e[31mwithout \e[0mpermission set\n"
    else
        echo -e "${WHITE}Other execute \e[0mpermission: \e[32mYES\e[0m\n"
    fi


    # last modified

    echo -e "${WHITE}Last modified\e[0m: $(echo "$STRING" | awk '{print $7 " " $6 " at " $8}')\n"

}

function  folder_modify () {
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
    echo -e "    \e[34mex  \e[0m- back to main menu"

    echo -en "\n>> "
    read -r choice

    case $choice in
        o)
            echo -en "Enter new owner: "
            read -r new_owner
            if getent passwd "$new_owner" &> /dev/null; then
                # command subsitution grabs the current group of dir
                sudo chown $new_owner:$(stat -c "%G" $CUR_PATH) $CUR_PATH
                touch "$CUR_PATH"
            else
                echo -e "No user by the name of \"$new_owner\""
            fi
            ;;
        g)
            echo -en "Enter new group: "
            read -r new_group
            if getent group "$new_group" &> /dev/null; then
                # command subsitution grabs the current owner of dir
                sudo chown $(stat -c "%U" $CUR_PATH):$new_group $CUR_PATH
                touch "$CUR_PATH"
            else
                echo -e "No group by the name or GID of \"$new_group\""
            fi
            ;;
        r1)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 2) == '-' ]; then
                sudo chmod u+r "$CUR_PATH"
            else
                sudo chmod u-r "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        w1)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 3) == '-' ]; then
                sudo chmod u+w "$CUR_PATH"
            else
                sudo chmod u-w "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        x1)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 4) == '-' ]; then
                sudo chmod u+x "$CUR_PATH"
            else
                sudo chmod u-x "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        r2)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 5) == '-' ]; then
                sudo chmod g+r "$CUR_PATH"
            else
                sudo chmod g-r "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        w2)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 6) == '-' ]; then
                sudo chmod g+w "$CUR_PATH"
            else
                sudo chmod g-w "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        x2)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 7) == '-' ] || [ $(stat -c "%A" $CUR_PATH | cut -b 7) == 'S' ]; then
                sudo chmod g+x "$CUR_PATH"
            else
                sudo chmod g-x "$CUR_PATH"
            fi
            touch $CUR_PATH
            ;;
        r3)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 8) == '-' ]; then
                sudo chmod o+r "$CUR_PATH"
            else
                sudo chmod o-r "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        w3)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 9) == '-' ]; then
                sudo chmod o+w "$CUR_PATH"
            else
                sudo chmod o-w "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        x3)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 10) == '-' ] || [ $(stat -c "%A" "$CUR_PATH" | cut -b 10) == 'T' ]; then
                sudo chmod o+x "$CUR_PATH"
            else
                sudo chmod o-x "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        G)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 7) == 's' ] || [ $(stat -c "%A" "$CUR_PATH" | cut -b 7) == 'S' ]; then
                sudo chmod g-s "$CUR_PATH"
            else
                sudo chmod g+s "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        T)
            if [ $(stat -c "%A" "$CUR_PATH" | cut -b 10) == 't' ] || [ $(stat -c "%A" "$CUR_PATH" | cut -b 10) == 'T' ]; then
                sudo chmod o-t "$CUR_PATH"
            else
                sudo chmod o+t "$CUR_PATH"
            fi
            touch "$CUR_PATH"
            ;;
        n)
            echo -n "Enter new name for directory: "
            read -r new_name
            # check if folder already exists
            if [ -d "$(dirname "$CUR_PATH")/$new_name" ] &> /dev/null; then
                echo -e "Directory \"$new_name\" already exists"
            else
                # if not, rename and update $CUR_PATH
                sudo mv "$CUR_PATH" "$(dirname "$CUR_PATH")/$new_name"
                CUR_PATH="$(dirname "$CUR_PATH")/$new_name"
                touch "$CUR_PATH"
            fi
            ;;
        ex)
            return
            ;;
        *)
            echo -e "Unknown choice \"$choice\""
            ;;
    esac

}

function folder_delete () {

    echo -en "You are about to \e[31mPermanently remove $CUR_PATH\n\e[0m(y/n) "
    read -r removal_confirmation

    case $removal_confirmation in
        y | Y)
            sudo rm -r "$CUR_PATH"
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
}



while true; do
    clear
    print_header
    print_menu
    read -rp "Choice: " user_choice

    print_dashed_line
    case $user_choice in
            # network inforamtion
        ni)
            net_info
            ;;

            #**** USER ******
        ua)
            user_add
            ;;
        ul)
            user_list
            ;;
        uv)
            user_view
            ;;
        um)
            user_modify_menu
            read -rp "choice: " you
            clear
            case $you in
                sa)
                    user_show_attr
                    ;;
                ea)
                    user_edit_attr
                    ;;
                cu)
                    user_change_username
                    ;;
                cp)
                    user_change_password
                    ;;
            esac
            ;;
        ud)
            user_delete
            ;;

            #**** GROUP ******
        ga)
            group_add
            ;;
        gl)
            group_list
            ;;
        gv)
            group_view
            ;;
        gm)
            group_modify
            ;;
        gd)
            group_delete
            ;;

            #**** FOLDER ******
        fa)
            folder_add
            ;;
        fl)
            folder_list
            ;;
        fv)
            folder_view
            ;;
        fm)
            folder_modify
            ;;
        fd)
            folder_delete
            ;;

        ex)
            echo "See you!"
            break
            ;;
        *)
            echo "Error: Invalid choice. Please try again."
            ;;
    esac
    print_dashed_line
    read -rp "Press Enter to continue..."
done
