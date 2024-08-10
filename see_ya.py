from colorama import Fore, Style, init


def see_ya():
    print(
        rf"""
{Style.BRIGHT}{Fore.YELLOW}
 #######  ##    ##     ###    
##    ##   ##  ##     ## ##   
##          ####     ##   ##  
##           ##     ## # # ##
##    ##     ##     ##     ## 
 ######      ##     ##     ##
 {Style.RESET_ALL}"""
    )


if __name__ == "__main__":
    see_ya()
