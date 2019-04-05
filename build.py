#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder(pure_c=False)
    build_shared = os.getenv("BUILD_SHARED", "True") == "True"
    builder.remove_build_if(lambda build: build.options["librealsense:shared"] != build_shared)
    builder.run()
