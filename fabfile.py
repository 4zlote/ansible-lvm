#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Name: ansible-lvm

from fabric.api import local

def git():
    """Configure Git"""

    local("git remote rm origin")
    local("git remote add origin https://korniichuk@github.com/korniichuk/ansible-lvm.git")
