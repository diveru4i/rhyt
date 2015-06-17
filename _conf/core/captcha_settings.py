# -*- coding: utf-8 -*-
import os

from core import STATIC_ROOT


CAPTCHA_OUTPUT_FORMAT = u'''
<div class="captcha">
    <div class="captcha-wrapper">
        %(image)s
        %(hidden_field)s
        <button class="captcha-refresh js-captcha-refresh" title="refresh" type="button" data-refresh-url=""></button>
    </div>
    <label class="form-help-text inline-field" for="id_captcha_1">
        %(text_field)s
    </label>
</div>
'''

CAPTCHA_FONT_PATH = os.path.join(STATIC_ROOT, 'core', 'fonts', 'BEAUTYSC.ttf')
    # ('Zebrra', os.path.join(STATIC_ROOT, 'core', 'fonts', 'zebrra.ttf')),
    # ('UnityDances', os.path.join(STATIC_ROOT, 'core', 'fonts', 'BEAUTYSC.ttf')),

CAPTCHA_LENGTH = 6
CAPTCHA_FONT_SIZE = 40

CAPTCHA_NOISE_FUNCTIONS = []
CAPTCHA_BACKGROUND_COLOR = '#f8f9fa'
# CAPTCHA_FOREGROUND_COLOR = '#ffffff'

u'''
<div class="captcha">
    <div class="captcha-wrapper">
        <img src="/markup/markup-images/captcha.png" alt="captcha" class="captcha-image">
        <input id="id_captcha_0" name="captcha_0" type="hidden" value="0">
        <button class="captcha-refresh js-captcha-refresh" title="refresh" type="button" data-refresh-url=""></button>
    </div>
    <label class="form-help-text inline-field" for="id_captcha_1">
        <input autocomplete="off" id="id_captcha_1" name="captcha_1" type="text" class="is-required is-captcha" required pattern="\w{6}">
    </label>
</div>
'''
