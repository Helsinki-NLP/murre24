#! /bin/bash

#for FOLDER in ns nswiki nswikiskn; do
#for FOLDER in lrec_ns lrec_nswiki lrec_nswikiskn; do
for FOLDER in <datafolder>; do
    echo $FOLDER
    for FOLD in a b c; do
	echo $FOLD
	cp languagelist.$FOLD languagelist
	cp ../$FOLDER/"training_"$FOLD".txt" Training
	cp ../$FOLDER/"test_"$FOLD".txt" Test
	echo 'Create models'
	java -cp guava-23.0.jar createmodels.java
	echo 'Predict'
	java -cp guava-23.0.jar HeLI.java | cut -f2 > $FOLD.pred
	echo 'Remove'
	rm Models/*
	rm Training/*
	rm Test/*
    done
done
