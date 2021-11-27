#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


class TrostatConfig():
    def __init__(self):
        #Client ID
        self.clinet_id = "client_id_here"

        #Banner check
        self.banner_check = True

        #Target check
        self.target_check = True

        #Live title check
        self.live_title_check = True

        #Category check
        self.category_check = True

        #Followers check
        self.followers_check = True

        #Current viewers check
        self.current_viewers_check = True

        #Subscribers check
        self.subscriber_check = True

        #start check
        self.start_check = True

        #Is live check
        self.is_live_check = True

    @staticmethod
    def ParseConfig(config_path):
        f = open(config_path, "rb")
        s = json.load(f)

        td = vars(TrostatConfig())
        td = td | s

        t = TrostatConfig()
        t.__dict__ = json.loads(json.dumps(td))

        return t
