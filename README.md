# domotics-gestures

Controlling domotics via gestures using a webcam

## Introduction

- keep things simple; something functional over exploring techniques which are more advanced than needed.
- this is a personal pet project - if it works for me it's good enough right now.
- it should run on a raspberry pi, so no fancy GPU requirements (except maybe for training to speed things up a bit)
- in other words: if you stumble across this, don't expect much :P

## Plan of attack

### MVP1 (todo: convert these to issues in github)

- tools to record positive and negative samples
- train on those samples
- cli tool to watch webcam and print out binary classification results
- report classification results to an external service (http calls) -- taking care to avoid too many calls

## Usage

Start by recording some samples using `record.py`. This tool will produce a 300 frame avi file. Make sure to move around a bit while keeping yourself in the positive/negative position.

	python src/record.py positive.avi
	python src/record.py negative.avi


