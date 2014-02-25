# -*- coding: utf-8 -*-

LOGIN_PAGE = "http://yuancheng.xunlei.com/login.html"
V2_PAGE = "http://yuancheng.xunlei.com/"
V3_PAGE = "http://yuancheng.xunlei.com/3/"

XWARED_LOCK = "/tmp/xware_xwared.lock"
XWARED_SOCKET = "/tmp/xware_xwared.socket"

ETM_CFG_DIR = "/opt/xware_desktop/xware/cfg"
ETM_LOCK = "/tmp/xware_ETM.lock"
ETM_CFG_FILE = "/opt/xware_desktop/xware/cfg/etm.cfg"

FRONTEND_LOCK = "/tmp/xware_frontend.lock"
FRONTEND_SOCKET = ("/tmp/xware_frontend.socket", "AF_UNIX")

CONFIG_FILE = "/opt/xware_desktop/settings.ini"

MOUNTS_FILE = "/opt/xware_desktop/mounts"
MOUNTS_FILE_HEADER = "# This file is automatically generated by Xware Desktop. Manually modifying this file via a text editor is not advised."

ETM_MOUNTS_DIR = "/tmp/thunder/volumes/" # the last slash is needed

PERMISSIONCHECK = "/opt/xware_desktop/permissioncheck"