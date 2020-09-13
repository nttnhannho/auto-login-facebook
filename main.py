from exception import FBLoginError

try:
    import login_action
except FBLoginError:
    print('[ERROR]Error happened while import \'login_action\' module')
    raise FBLoginError
