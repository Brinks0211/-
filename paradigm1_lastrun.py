#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on 五月 27, 2021, at 19:57
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

x2=100
n2=0.25
x3=100
n3=0.25


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'paradigm1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Num': '', 'gender': '', 'age': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\张以昊\\大二下学期\\决策心理学\\延时折扣任务\\paradigm1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "introduction1"
introduction1Clock = core.Clock()
introduction1_1 = visual.ImageStim(
    win=win,
    name='introduction1_1', 
    image='document\\introduction1_1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_1 = keyboard.Keyboard()

# Initialize components for Routine "device_use_time1"
device_use_time1Clock = core.Clock()
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.5, pos=[0.0, 0.0], choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '12+'], tickHeight=-1)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='document\\\\device_use_time.png', mask=None,
    ori=0.0, pos=(0, 0.2), size=(2.15,0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "introduction4"
introduction4Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='document\\\\introduction4_1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "device_questionaire"
device_questionaireClock = core.Clock()
device_question = visual.ImageStim(
    win=win,
    name='device_question', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.76,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
question_key = keyboard.Keyboard()

# Initialize components for Routine "introduction2"
introduction2Clock = core.Clock()
introduction2_1 = visual.ImageStim(
    win=win,
    name='introduction2_1', 
    image='document\\introduction2_1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.76, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "time_percition"
time_percitionClock = core.Clock()
concentration = visual.TextStim(win=win, name='concentration',
    text='+',
    font=None,
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trumpet = visual.ImageStim(
    win=win,
    name='trumpet', 
    image='document\\laba.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='sound_1')
sound_1.setVolume(5)

# Initialize components for Routine "repeat_start"
repeat_startClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='请按下左键开始声音复制\n请按下右键结束声音复制',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
repeat_sound_start = keyboard.Keyboard()

# Initialize components for Routine "repeat_time"
repeat_timeClock = core.Clock()
text1 = visual.TextStim(win=win, name='text1',
    text='声音正在复制\n',
    font='hei',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('A', secs=-1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image_copy = visual.ImageStim(
    win=win,
    name='image_copy', 
    image='document\\\\laba.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_sound_end = keyboard.Keyboard()

# Initialize components for Routine "introduction3"
introduction3Clock = core.Clock()
introduction3_1 = visual.ImageStim(
    win=win,
    name='introduction3_1', 
    image='document\\\\introduction3_1.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1.76,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "one_week"
one_weekClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='立即获得',
    font='Open Sans',
    pos=(-0.4, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='一周后金额',
    font='Open Sans',
    pos=(0.4, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='yellow', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='200',
    font='Open Sans',
    pos=(0.4, -0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
x1=100
n1=0.25
one_week_key = keyboard.Keyboard()

# Initialize components for Routine "one_month_3"
one_month_3Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='立即获得金额',
    font='Open Sans',
    pos=(-0.4, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instance = visual.TextStim(win=win, name='instance',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='一个月后金额',
    font='Open Sans',
    pos=(0.4, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
one_month = visual.TextStim(win=win, name='one_month',
    text='200',
    font='Open Sans',
    pos=(0.4, -0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
one_month_key = keyboard.Keyboard()

# Initialize components for Routine "six_months"
six_monthsClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='立即获得金额',
    font='Open Sans',
    pos=(-0.4, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='六个月后金额\n',
    font='Open Sans',
    pos=(0.4, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='coral', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Open Sans',
    pos=(-0.4, -0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='200',
    font='Open Sans',
    pos=(0.4, -0.2), height=0.07, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
six_months_key = keyboard.Keyboard()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='实验结束，感谢您的参与！',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "introduction1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_1.keys = []
key_resp_1.rt = []
_key_resp_1_allKeys = []
# keep track of which components have finished
introduction1Components = [introduction1_1, key_resp_1]
for thisComponent in introduction1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction1"-------
while continueRoutine:
    # get current time
    t = introduction1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction1_1* updates
    if introduction1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction1_1.frameNStart = frameN  # exact frame index
        introduction1_1.tStart = t  # local t and not account for scr refresh
        introduction1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction1_1, 'tStartRefresh')  # time at next scr refresh
        introduction1_1.setAutoDraw(True)
    
    # *key_resp_1* updates
    waitOnFlip = False
    if key_resp_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.tStart = t  # local t and not account for scr refresh
        key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_1_allKeys.extend(theseKeys)
        if len(_key_resp_1_allKeys):
            key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
            key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction1"-------
for thisComponent in introduction1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "device_use_time1"-------
continueRoutine = True
# update component parameters for each repeat
rating.reset()
# keep track of which components have finished
device_use_time1Components = [rating, image]
for thisComponent in device_use_time1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
device_use_time1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "device_use_time1"-------
while continueRoutine:
    # get current time
    t = device_use_time1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=device_use_time1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *rating* updates
    if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rating.frameNStart = frameN  # exact frame index
        rating.tStart = t  # local t and not account for scr refresh
        rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
        rating.setAutoDraw(True)
    continueRoutine &= rating.noResponse  # a response ends the trial
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in device_use_time1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "device_use_time1"-------
for thisComponent in device_use_time1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.nextEntry()
# the Routine "device_use_time1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction4"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
introduction4Components = [image_2, key_resp_3]
for thisComponent in introduction4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction4"-------
while continueRoutine:
    # get current time
    t = introduction4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if key_resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clock.reset()  # now t=0
    if key_resp_3.status == STARTED:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction4"-------
for thisComponent in introduction4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop5 = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('document\\\\questionaire.xlsx'),
    seed=None, name='loop5')
thisExp.addLoop(loop5)  # add the loop to the experiment
thisLoop5 = loop5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop5.rgb)
if thisLoop5 != None:
    for paramName in thisLoop5:
        exec('{} = thisLoop5[paramName]'.format(paramName))

for thisLoop5 in loop5:
    currentLoop = loop5
    # abbreviate parameter names if possible (e.g. rgb = thisLoop5.rgb)
    if thisLoop5 != None:
        for paramName in thisLoop5:
            exec('{} = thisLoop5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "device_questionaire"-------
    continueRoutine = True
    # update component parameters for each repeat
    device_question.setImage(question)
    question_key.keys = []
    question_key.rt = []
    _question_key_allKeys = []
    # keep track of which components have finished
    device_questionaireComponents = [device_question, question_key]
    for thisComponent in device_questionaireComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    device_questionaireClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "device_questionaire"-------
    while continueRoutine:
        # get current time
        t = device_questionaireClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=device_questionaireClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *device_question* updates
        if device_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            device_question.frameNStart = frameN  # exact frame index
            device_question.tStart = t  # local t and not account for scr refresh
            device_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(device_question, 'tStartRefresh')  # time at next scr refresh
            device_question.setAutoDraw(True)
        
        # *question_key* updates
        if question_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_key.frameNStart = frameN  # exact frame index
            question_key.tStart = t  # local t and not account for scr refresh
            question_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_key, 'tStartRefresh')  # time at next scr refresh
            question_key.status = STARTED
            # keyboard checking is just starting
            question_key.clock.reset()  # now t=0
        if question_key.status == STARTED:
            theseKeys = question_key.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _question_key_allKeys.extend(theseKeys)
            if len(_question_key_allKeys):
                question_key.keys = _question_key_allKeys[-1].name  # just the last key pressed
                question_key.rt = _question_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in device_questionaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "device_questionaire"-------
    for thisComponent in device_questionaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if question_key.keys in ['', [], None]:  # No response was made
        question_key.keys = None
    loop5.addData('question_key.keys',question_key.keys)
    if question_key.keys != None:  # we had a response
        loop5.addData('question_key.rt', question_key.rt)
    # the Routine "device_questionaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop5'


# ------Prepare to start Routine "introduction2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
introduction2Components = [introduction2_1, key_resp_2]
for thisComponent in introduction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction2"-------
while continueRoutine:
    # get current time
    t = introduction2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction2_1* updates
    if introduction2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction2_1.frameNStart = frameN  # exact frame index
        introduction2_1.tStart = t  # local t and not account for scr refresh
        introduction2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction2_1, 'tStartRefresh')  # time at next scr refresh
        introduction2_1.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction2"-------
for thisComponent in introduction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('document\\material.xlsx'),
    seed=None, name='loop1')
thisExp.addLoop(loop1)  # add the loop to the experiment
thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
if thisLoop1 != None:
    for paramName in thisLoop1:
        exec('{} = thisLoop1[paramName]'.format(paramName))

for thisLoop1 in loop1:
    currentLoop = loop1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
    if thisLoop1 != None:
        for paramName in thisLoop1:
            exec('{} = thisLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "time_percition"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_1.setSound('A', secs=emerge, hamming=False)
    sound_1.setVolume(5, log=False)
    # keep track of which components have finished
    time_percitionComponents = [concentration, trumpet, sound_1]
    for thisComponent in time_percitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    time_percitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "time_percition"-------
    while continueRoutine:
        # get current time
        t = time_percitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=time_percitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *concentration* updates
        if concentration.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            concentration.frameNStart = frameN  # exact frame index
            concentration.tStart = t  # local t and not account for scr refresh
            concentration.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(concentration, 'tStartRefresh')  # time at next scr refresh
            concentration.setAutoDraw(True)
        if concentration.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > concentration.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                concentration.tStop = t  # not accounting for scr refresh
                concentration.frameNStop = frameN  # exact frame index
                win.timeOnFlip(concentration, 'tStopRefresh')  # time at next scr refresh
                concentration.setAutoDraw(False)
        
        # *trumpet* updates
        if trumpet.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            trumpet.frameNStart = frameN  # exact frame index
            trumpet.tStart = t  # local t and not account for scr refresh
            trumpet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trumpet, 'tStartRefresh')  # time at next scr refresh
            trumpet.setAutoDraw(True)
        if trumpet.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trumpet.tStartRefresh + emerge-frameTolerance:
                # keep track of stop time/frame for later
                trumpet.tStop = t  # not accounting for scr refresh
                trumpet.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trumpet, 'tStopRefresh')  # time at next scr refresh
                trumpet.setAutoDraw(False)
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and t >= 2-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play()  # start the sound (it finishes automatically)
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + emerge-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in time_percitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "time_percition"-------
    for thisComponent in time_percitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # the Routine "time_percition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "repeat_start"-------
    continueRoutine = True
    # update component parameters for each repeat
    repeat_sound_start.keys = []
    repeat_sound_start.rt = []
    _repeat_sound_start_allKeys = []
    # keep track of which components have finished
    repeat_startComponents = [text, repeat_sound_start]
    for thisComponent in repeat_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    repeat_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "repeat_start"-------
    while continueRoutine:
        # get current time
        t = repeat_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=repeat_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *repeat_sound_start* updates
        waitOnFlip = False
        if repeat_sound_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            repeat_sound_start.frameNStart = frameN  # exact frame index
            repeat_sound_start.tStart = t  # local t and not account for scr refresh
            repeat_sound_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repeat_sound_start, 'tStartRefresh')  # time at next scr refresh
            repeat_sound_start.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(repeat_sound_start.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(repeat_sound_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if repeat_sound_start.status == STARTED and not waitOnFlip:
            theseKeys = repeat_sound_start.getKeys(keyList=['left'], waitRelease=False)
            _repeat_sound_start_allKeys.extend(theseKeys)
            if len(_repeat_sound_start_allKeys):
                repeat_sound_start.keys = _repeat_sound_start_allKeys[-1].name  # just the last key pressed
                repeat_sound_start.rt = _repeat_sound_start_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeat_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "repeat_start"-------
    for thisComponent in repeat_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "repeat_start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "repeat_time"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    sound_2.setSound('A', secs=20.0, hamming=True)
    sound_2.setVolume(1.0, log=False)
    key_resp_sound_end.keys = []
    key_resp_sound_end.rt = []
    _key_resp_sound_end_allKeys = []
    # keep track of which components have finished
    repeat_timeComponents = [text1, sound_2, image_copy, key_resp_sound_end]
    for thisComponent in repeat_timeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    repeat_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "repeat_time"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = repeat_timeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=repeat_timeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text1* updates
        if text1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text1.frameNStart = frameN  # exact frame index
            text1.tStart = t  # local t and not account for scr refresh
            text1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text1, 'tStartRefresh')  # time at next scr refresh
            text1.setAutoDraw(True)
        if text1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text1.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text1.tStop = t  # not accounting for scr refresh
                text1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text1, 'tStopRefresh')  # time at next scr refresh
                text1.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # *image_copy* updates
        if image_copy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_copy.frameNStart = frameN  # exact frame index
            image_copy.tStart = t  # local t and not account for scr refresh
            image_copy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_copy, 'tStartRefresh')  # time at next scr refresh
            image_copy.setAutoDraw(True)
        if image_copy.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_copy.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                image_copy.tStop = t  # not accounting for scr refresh
                image_copy.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_copy, 'tStopRefresh')  # time at next scr refresh
                image_copy.setAutoDraw(False)
        
        # *key_resp_sound_end* updates
        waitOnFlip = False
        if key_resp_sound_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_sound_end.frameNStart = frameN  # exact frame index
            key_resp_sound_end.tStart = t  # local t and not account for scr refresh
            key_resp_sound_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_sound_end, 'tStartRefresh')  # time at next scr refresh
            key_resp_sound_end.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_sound_end.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_sound_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_sound_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_sound_end.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_sound_end.tStop = t  # not accounting for scr refresh
                key_resp_sound_end.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_sound_end, 'tStopRefresh')  # time at next scr refresh
                key_resp_sound_end.status = FINISHED
        if key_resp_sound_end.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_sound_end.getKeys(keyList=['right'], waitRelease=False)
            _key_resp_sound_end_allKeys.extend(theseKeys)
            if len(_key_resp_sound_end_allKeys):
                key_resp_sound_end.keys = _key_resp_sound_end_allKeys[-1].name  # just the last key pressed
                key_resp_sound_end.rt = _key_resp_sound_end_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeat_timeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "repeat_time"-------
    for thisComponent in repeat_timeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    # check responses
    if key_resp_sound_end.keys in ['', [], None]:  # No response was made
        key_resp_sound_end.keys = None
    loop1.addData('key_resp_sound_end.keys',key_resp_sound_end.keys)
    if key_resp_sound_end.keys != None:  # we had a response
        loop1.addData('key_resp_sound_end.rt', key_resp_sound_end.rt)
    thisExp.nextEntry()
    
# completed 2 repeats of 'loop1'


# ------Prepare to start Routine "introduction3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introduction3Components = [introduction3_1, key_resp]
for thisComponent in introduction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introduction3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "introduction3"-------
while continueRoutine:
    # get current time
    t = introduction3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introduction3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction3_1* updates
    if introduction3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction3_1.frameNStart = frameN  # exact frame index
        introduction3_1.tStart = t  # local t and not account for scr refresh
        introduction3_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction3_1, 'tStartRefresh')  # time at next scr refresh
        introduction3_1.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introduction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction3"-------
for thisComponent in introduction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "introduction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop3 = data.TrialHandler(nReps=6.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop3')
thisExp.addLoop(loop3)  # add the loop to the experiment
thisLoop3 = loop3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
if thisLoop3 != None:
    for paramName in thisLoop3:
        exec('{} = thisLoop3[paramName]'.format(paramName))

for thisLoop3 in loop3:
    currentLoop = loop3
    # abbreviate parameter names if possible (e.g. rgb = thisLoop3.rgb)
    if thisLoop3 != None:
        for paramName in thisLoop3:
            exec('{} = thisLoop3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "one_week"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_6.setText(x1)
    one_week_key.keys = []
    one_week_key.rt = []
    _one_week_key_allKeys = []
    # keep track of which components have finished
    one_weekComponents = [text_5, text_6, text_7, text_8, one_week_key]
    for thisComponent in one_weekComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    one_weekClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "one_week"-------
    while continueRoutine:
        # get current time
        t = one_weekClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=one_weekClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        
        # *one_week_key* updates
        if one_week_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one_week_key.frameNStart = frameN  # exact frame index
            one_week_key.tStart = t  # local t and not account for scr refresh
            one_week_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_week_key, 'tStartRefresh')  # time at next scr refresh
            one_week_key.status = STARTED
            # keyboard checking is just starting
            one_week_key.clock.reset()  # now t=0
            one_week_key.clearEvents(eventType='keyboard')
        if one_week_key.status == STARTED:
            theseKeys = one_week_key.getKeys(keyList=['left', 'right'], waitRelease=False)
            _one_week_key_allKeys.extend(theseKeys)
            if len(_one_week_key_allKeys):
                one_week_key.keys = _one_week_key_allKeys[-1].name  # just the last key pressed
                one_week_key.rt = _one_week_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in one_weekComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "one_week"-------
    for thisComponent in one_weekComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if 'left' in one_week_key.keys:
        x1 = round(x1-200*n1,2)
        n1 = n1/2
    if 'right' in one_week_key.keys:
        x1 = round(x1+200*n1,2)
        n1 = n1/2
    # check responses
    if one_week_key.keys in ['', [], None]:  # No response was made
        one_week_key.keys = None
    loop3.addData('one_week_key.keys',one_week_key.keys)
    if one_week_key.keys != None:  # we had a response
        loop3.addData('one_week_key.rt', one_week_key.rt)
    # the Routine "one_week" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'loop3'


# set up handler to look after randomisation of conditions etc
loop2 = data.TrialHandler(nReps=6.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop2')
thisExp.addLoop(loop2)  # add the loop to the experiment
thisLoop2 = loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
if thisLoop2 != None:
    for paramName in thisLoop2:
        exec('{} = thisLoop2[paramName]'.format(paramName))

for thisLoop2 in loop2:
    currentLoop = loop2
    # abbreviate parameter names if possible (e.g. rgb = thisLoop2.rgb)
    if thisLoop2 != None:
        for paramName in thisLoop2:
            exec('{} = thisLoop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "one_month_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    instance.setText(x2)
    one_month_key.keys = []
    one_month_key.rt = []
    _one_month_key_allKeys = []
    # keep track of which components have finished
    one_month_3Components = [text_2, instance, text_3, one_month, one_month_key]
    for thisComponent in one_month_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    one_month_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "one_month_3"-------
    while continueRoutine:
        # get current time
        t = one_month_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=one_month_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *instance* updates
        if instance.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instance.frameNStart = frameN  # exact frame index
            instance.tStart = t  # local t and not account for scr refresh
            instance.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instance, 'tStartRefresh')  # time at next scr refresh
            instance.setAutoDraw(True)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *one_month* updates
        if one_month.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one_month.frameNStart = frameN  # exact frame index
            one_month.tStart = t  # local t and not account for scr refresh
            one_month.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_month, 'tStartRefresh')  # time at next scr refresh
            one_month.setAutoDraw(True)
        
        # *one_month_key* updates
        waitOnFlip = False
        if one_month_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one_month_key.frameNStart = frameN  # exact frame index
            one_month_key.tStart = t  # local t and not account for scr refresh
            one_month_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one_month_key, 'tStartRefresh')  # time at next scr refresh
            one_month_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(one_month_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(one_month_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if one_month_key.status == STARTED and not waitOnFlip:
            theseKeys = one_month_key.getKeys(keyList=['left', 'right'], waitRelease=False)
            _one_month_key_allKeys.extend(theseKeys)
            if len(_one_month_key_allKeys):
                one_month_key.keys = _one_month_key_allKeys[-1].name  # just the last key pressed
                one_month_key.rt = _one_month_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in one_month_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "one_month_3"-------
    for thisComponent in one_month_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if 'left' in one_month_key.keys:
        x2 = round(x2-200*n2,2)
        n2 = n2/2
    if 'right' in one_month_key.keys:
        x2 = round(x2+200*n2,2)
        n2 = n2/2
    # check responses
    if one_month_key.keys in ['', [], None]:  # No response was made
        one_month_key.keys = None
    loop2.addData('one_month_key.keys',one_month_key.keys)
    if one_month_key.keys != None:  # we had a response
        loop2.addData('one_month_key.rt', one_month_key.rt)
    # the Routine "one_month_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'loop2'


# set up handler to look after randomisation of conditions etc
loop4 = data.TrialHandler(nReps=6.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='loop4')
thisExp.addLoop(loop4)  # add the loop to the experiment
thisLoop4 = loop4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop4.rgb)
if thisLoop4 != None:
    for paramName in thisLoop4:
        exec('{} = thisLoop4[paramName]'.format(paramName))

for thisLoop4 in loop4:
    currentLoop = loop4
    # abbreviate parameter names if possible (e.g. rgb = thisLoop4.rgb)
    if thisLoop4 != None:
        for paramName in thisLoop4:
            exec('{} = thisLoop4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "six_months"-------
    continueRoutine = True
    # update component parameters for each repeat
    text_12.setText(x3)
    six_months_key.keys = []
    six_months_key.rt = []
    _six_months_key_allKeys = []
    # keep track of which components have finished
    six_monthsComponents = [text_10, text_11, text_12, text_13, six_months_key]
    for thisComponent in six_monthsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    six_monthsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "six_months"-------
    while continueRoutine:
        # get current time
        t = six_monthsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=six_monthsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        
        # *text_13* updates
        if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_13.frameNStart = frameN  # exact frame index
            text_13.tStart = t  # local t and not account for scr refresh
            text_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
            text_13.setAutoDraw(True)
        
        # *six_months_key* updates
        if six_months_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            six_months_key.frameNStart = frameN  # exact frame index
            six_months_key.tStart = t  # local t and not account for scr refresh
            six_months_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(six_months_key, 'tStartRefresh')  # time at next scr refresh
            six_months_key.status = STARTED
            # keyboard checking is just starting
            six_months_key.clock.reset()  # now t=0
            six_months_key.clearEvents(eventType='keyboard')
        if six_months_key.status == STARTED:
            theseKeys = six_months_key.getKeys(keyList=['left', 'right'], waitRelease=False)
            _six_months_key_allKeys.extend(theseKeys)
            if len(_six_months_key_allKeys):
                six_months_key.keys = _six_months_key_allKeys[-1].name  # just the last key pressed
                six_months_key.rt = _six_months_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in six_monthsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "six_months"-------
    for thisComponent in six_monthsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if six_months_key.keys in ['', [], None]:  # No response was made
        six_months_key.keys = None
    loop4.addData('six_months_key.keys',six_months_key.keys)
    if six_months_key.keys != None:  # we had a response
        loop4.addData('six_months_key.rt', six_months_key.rt)
    if 'left' in six_months_key.keys:
        x3 = round(x3-200*n3,2)
        n3 = n3/2
    if 'right' in six_months_key.keys:
        x3 = round(x3+200*n3,2)
        n3 = n3/2
    # the Routine "six_months" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'loop4'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_4]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
