#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Feb  2 20:32:40 2022
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'rdm_test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/meetakshi/Documents/PSYCHOPY/dot/rdm_test_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcomeScreen"
welcomeScreenClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='<Insert Instructions Here>\n\nPress any key to start the experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
welcomeResponse = keyboard.Keyboard()

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trialCoherentMotion"
trialCoherentMotionClock = core.Clock()
dotsCoherent = visual.DotStim(
    win=win, name='dotsCoherent',
    nDots=118, dotSize=6.0,
    speed=0.02, dir=1.0, coherence=1.0,
    fieldPos=(0.0, 0.0), fieldSize=1.0,fieldShape='circle',
    signalDots='same', noiseDots='direction',dotLife=3.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
    depth=0.0)
responseCoherent = keyboard.Keyboard()

# Initialize components for Routine "trialIncoherentMotion"
trialIncoherentMotionClock = core.Clock()
dotsIncoherent = visual.DotStim(
    win=win, name='dotsIncoherent',
    nDots=118, dotSize=6.0,
    speed=0.02, dir=0.0, coherence=0.0,
    fieldPos=(0.0, 0.0), fieldSize=1.0,fieldShape='circle',
    signalDots='same', noiseDots='direction',dotLife=3.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=None,
    depth=0.0)

# Initialize components for Routine "blank500"
blank500Clock = core.Clock()
textBlank500 = visual.TextStim(win=win, name='textBlank500',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "endScreen"
endScreenClock = core.Clock()
textEndScreen = visual.TextStim(win=win, name='textEndScreen',
    text='Thank you for your time. Press any key to exit.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
keyEndScreenResponse = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
welcomeResponse.keys = []
welcomeResponse.rt = []
_welcomeResponse_allKeys = []
# keep track of which components have finished
welcomeScreenComponents = [text, welcomeResponse]
for thisComponent in welcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcomeScreen"-------
while continueRoutine:
    # get current time
    t = welcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeScreenClock)
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
    
    # *welcomeResponse* updates
    waitOnFlip = False
    if welcomeResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeResponse.frameNStart = frameN  # exact frame index
        welcomeResponse.tStart = t  # local t and not account for scr refresh
        welcomeResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeResponse, 'tStartRefresh')  # time at next scr refresh
        welcomeResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeResponse.status == STARTED and not waitOnFlip:
        theseKeys = welcomeResponse.getKeys(keyList=None, waitRelease=False)
        _welcomeResponse_allKeys.extend(theseKeys)
        if len(_welcomeResponse_allKeys):
            welcomeResponse.keys = _welcomeResponse_allKeys[-1].name  # just the last key pressed
            welcomeResponse.rt = _welcomeResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcomeScreen"-------
for thisComponent in welcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textBlank500]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank500"-------
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loopTemplate.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trialCoherentMotion"-------
    continueRoutine = True
    routineTimer.add(1.900000)
    # update component parameters for each repeat
    dotsCoherent.setDir(Direction)
    dotsCoherent.setFieldCoherence(Coherence)
    dotsCoherent.refreshDots()
    responseCoherent.keys = []
    responseCoherent.rt = []
    _responseCoherent_allKeys = []
    # keep track of which components have finished
    trialCoherentMotionComponents = [dotsCoherent, responseCoherent]
    for thisComponent in trialCoherentMotionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialCoherentMotionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialCoherentMotion"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialCoherentMotionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialCoherentMotionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dotsCoherent* updates
        if dotsCoherent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dotsCoherent.frameNStart = frameN  # exact frame index
            dotsCoherent.tStart = t  # local t and not account for scr refresh
            dotsCoherent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dotsCoherent, 'tStartRefresh')  # time at next scr refresh
            dotsCoherent.setAutoDraw(True)
        if dotsCoherent.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dotsCoherent.tStartRefresh + 1.9-frameTolerance:
                # keep track of stop time/frame for later
                dotsCoherent.tStop = t  # not accounting for scr refresh
                dotsCoherent.frameNStop = frameN  # exact frame index
                win.timeOnFlip(dotsCoherent, 'tStopRefresh')  # time at next scr refresh
                dotsCoherent.setAutoDraw(False)
        
        # *responseCoherent* updates
        waitOnFlip = False
        if responseCoherent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            responseCoherent.frameNStart = frameN  # exact frame index
            responseCoherent.tStart = t  # local t and not account for scr refresh
            responseCoherent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responseCoherent, 'tStartRefresh')  # time at next scr refresh
            responseCoherent.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(responseCoherent.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(responseCoherent.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if responseCoherent.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > responseCoherent.tStartRefresh + 1.9-frameTolerance:
                # keep track of stop time/frame for later
                responseCoherent.tStop = t  # not accounting for scr refresh
                responseCoherent.frameNStop = frameN  # exact frame index
                win.timeOnFlip(responseCoherent, 'tStopRefresh')  # time at next scr refresh
                responseCoherent.status = FINISHED
        if responseCoherent.status == STARTED and not waitOnFlip:
            theseKeys = responseCoherent.getKeys(keyList=['left', 'right'], waitRelease=False)
            _responseCoherent_allKeys.extend(theseKeys)
            if len(_responseCoherent_allKeys):
                responseCoherent.keys = _responseCoherent_allKeys[0].name  # just the first key pressed
                responseCoherent.rt = _responseCoherent_allKeys[0].rt
                # was this correct?
                if (responseCoherent.keys == str(CorrectAns)) or (responseCoherent.keys == CorrectAns):
                    responseCoherent.corr = 1
                else:
                    responseCoherent.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialCoherentMotionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialCoherentMotion"-------
    for thisComponent in trialCoherentMotionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('dotsCoherent.started', dotsCoherent.tStartRefresh)
    trials.addData('dotsCoherent.stopped', dotsCoherent.tStopRefresh)
    # check responses
    if responseCoherent.keys in ['', [], None]:  # No response was made
        responseCoherent.keys = None
        # was no response the correct answer?!
        if str(CorrectAns).lower() == 'none':
           responseCoherent.corr = 1;  # correct non-response
        else:
           responseCoherent.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('responseCoherent.keys',responseCoherent.keys)
    trials.addData('responseCoherent.corr', responseCoherent.corr)
    if responseCoherent.keys != None:  # we had a response
        trials.addData('responseCoherent.rt', responseCoherent.rt)
    trials.addData('responseCoherent.started', responseCoherent.tStartRefresh)
    trials.addData('responseCoherent.stopped', responseCoherent.tStopRefresh)
    
    # ------Prepare to start Routine "trialIncoherentMotion"-------
    continueRoutine = True
    # update component parameters for each repeat
    dotsIncoherent.refreshDots()
    # keep track of which components have finished
    trialIncoherentMotionComponents = [dotsIncoherent]
    for thisComponent in trialIncoherentMotionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialIncoherentMotionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trialIncoherentMotion"-------
    while continueRoutine:
        # get current time
        t = trialIncoherentMotionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialIncoherentMotionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dotsIncoherent* updates
        if dotsIncoherent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            dotsIncoherent.frameNStart = frameN  # exact frame index
            dotsIncoherent.tStart = t  # local t and not account for scr refresh
            dotsIncoherent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dotsIncoherent, 'tStartRefresh')  # time at next scr refresh
            dotsIncoherent.setAutoDraw(True)
        if dotsIncoherent.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dotsIncoherent.tStartRefresh + IncoherentMotionTime-frameTolerance:
                # keep track of stop time/frame for later
                dotsIncoherent.tStop = t  # not accounting for scr refresh
                dotsIncoherent.frameNStop = frameN  # exact frame index
                win.timeOnFlip(dotsIncoherent, 'tStopRefresh')  # time at next scr refresh
                dotsIncoherent.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialIncoherentMotionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trialIncoherentMotion"-------
    for thisComponent in trialIncoherentMotionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('dotsIncoherent.started', dotsIncoherent.tStartRefresh)
    trials.addData('dotsIncoherent.stopped', dotsIncoherent.tStopRefresh)
    # the Routine "trialIncoherentMotion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "blank500"-------
continueRoutine = True
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [textBlank500]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blank500Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blank500"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blank500Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blank500Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank500* updates
    if textBlank500.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank500.frameNStart = frameN  # exact frame index
        textBlank500.tStart = t  # local t and not account for scr refresh
        textBlank500.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank500, 'tStartRefresh')  # time at next scr refresh
        textBlank500.setAutoDraw(True)
    if textBlank500.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank500.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank500.tStop = t  # not accounting for scr refresh
            textBlank500.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank500, 'tStopRefresh')  # time at next scr refresh
            textBlank500.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blank500"-------
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "endScreen"-------
continueRoutine = True
# update component parameters for each repeat
keyEndScreenResponse.keys = []
keyEndScreenResponse.rt = []
_keyEndScreenResponse_allKeys = []
# keep track of which components have finished
endScreenComponents = [textEndScreen, keyEndScreenResponse]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "endScreen"-------
while continueRoutine:
    # get current time
    t = endScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndScreen* updates
    if textEndScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEndScreen.frameNStart = frameN  # exact frame index
        textEndScreen.tStart = t  # local t and not account for scr refresh
        textEndScreen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEndScreen, 'tStartRefresh')  # time at next scr refresh
        textEndScreen.setAutoDraw(True)
    if textEndScreen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEndScreen.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            textEndScreen.tStop = t  # not accounting for scr refresh
            textEndScreen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEndScreen, 'tStopRefresh')  # time at next scr refresh
            textEndScreen.setAutoDraw(False)
    
    # *keyEndScreenResponse* updates
    waitOnFlip = False
    if keyEndScreenResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyEndScreenResponse.frameNStart = frameN  # exact frame index
        keyEndScreenResponse.tStart = t  # local t and not account for scr refresh
        keyEndScreenResponse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyEndScreenResponse, 'tStartRefresh')  # time at next scr refresh
        keyEndScreenResponse.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyEndScreenResponse.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyEndScreenResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyEndScreenResponse.status == STARTED and not waitOnFlip:
        theseKeys = keyEndScreenResponse.getKeys(keyList=None, waitRelease=False)
        _keyEndScreenResponse_allKeys.extend(theseKeys)
        if len(_keyEndScreenResponse_allKeys):
            keyEndScreenResponse.keys = _keyEndScreenResponse_allKeys[-1].name  # just the last key pressed
            keyEndScreenResponse.rt = _keyEndScreenResponse_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endScreen"-------
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "endScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
