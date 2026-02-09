class InstagramAccount:
    def __init__(self,account_name,password):
        self.account_name=account_name
        self.__password=password
        self._private_reels=[]
        self.__archived_reels=[]
    def set_add_private_reel(self,reel_name):
        # self._private_reels.append(reel_name)
        self._private_reels.append(reel_name)
        print("Private reel added",self._private_reels)
    def get_display_private_reel(self,is_follower):
        if is_follower :
            print("private_reels:")
            for reel in self._private_reels:
                print("-",reel)
        else:
            print("access denied! only follower can view private reels")
    def set_dd_archived_reel(self,reel_name):
        self.__archived_reels.append(reel_name)

    def get_display_archived_reels(self,password):
        if password==self.__password:
            return self.__archived_reels
        else:
            return "access denied"
IA=InstagramAccount("manya",1234)
IA.set_add_private_reel("hi")
IA.set_add_private_reel("hi")
IA.get_display_private_reel(is_follower=True)
print(IA.get_display_archived_reels(2345))