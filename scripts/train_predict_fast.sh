#! /bin/bash

# Note that fastText wants the labels prefixed with __label__
for FOLDER in <datafolder>; do
    echo $FOLDER
    for FOLD in a b c; do
	echo $FOLD
	./fasttext supervised -input $FOLDER/"training_"$FOLD".txt" -output "model_"$FOLDER"_"$FOLD -lr 1.0 -epoch 25
	./fasttext predict "model_"$FOLDER"_"$FOLD.bin $FOLDER/"test_"$FOLD".txt" | sed 's/__label__//g' > "fast"$FOLDER"_"$FOLD.pred
    done
done
