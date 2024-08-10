from colorama import Fore, Style


def see_ya():
    print(
        rf"""
{Fore.RED} #######  ##    ##     ###    
{Fore.GREEN}##    ##   ##  ##     ## ##   
{Fore.BLUE}##          ####     ##   ##  
{Fore.MAGENTA}##           ##     ## # # ##
{Fore.CYAN}##    ##     ##     ##     ## 
{Fore.YELLOW} ######      ##     ##     ##
{Style.RESET_ALL}"""
    )


if __name__ == "__main__":
    see_ya()
