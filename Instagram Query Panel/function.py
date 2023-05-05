
import instaloader
import ctypes




############################################################################ 


def pp_down(username): 
    ig = instaloader.Instaloader()
    dp = username
    
    return ig.download_profile(dp , profile_pic_only=True)





###########################################################################

    
def say(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    return profile.mediacount

##############################################################################


def main(username):
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context, username)

        return {
            'profile': {
                'name': profile.full_name,
                'profileurl': f'https://www.instagram.com/{profile.username}/',
                'username': profile.username,
                'followers': f'{profile.followers}',
                'following': f'{profile.followees}',
                'posts': f'{profile.mediacount}',
                'aboutinfo': profile.biography
            }
        }
    except:
            MB_ICONERROR = 0x10
            MB_SETFOREGROUND = 0x100
            message = "Error!"
            title = "Profile has not found!"
            ctypes.windll.user32.MessageBoxW(None, message, title, MB_ICONERROR | MB_SETFOREGROUND, 500, 300)

###################################################################################