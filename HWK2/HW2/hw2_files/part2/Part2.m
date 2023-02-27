clear
unedited = imread('image_part2.png');
binaryStrict = imbinarize(unedited, .8);
binaryStrict = binaryStrict(:,:,1);
binaryLoose = imbinarize(unedited, .9);
binaryLoose = binaryLoose(:,:,1);
size = [size(binaryStrict, 1), size(binaryStrict, 2)];
squaresHighlighted = zeros(size(1), size(2));
colorsChanged = unedited;
for i=1:size(1)
    for j = 1:size(2)
        if (binaryStrict(i, j) == 1) && binaryLoose(i, j) == 0
            squaresHighlighted(i, j) = 1;
        end
        if (unedited(i, j, 1) == 106) && (unedited(i, j, 2) == 170) && (unedited(i, j, 3) == 100)
            colorsChanged(i,j,:) = [0,0,255];
        end
        if (unedited(i, j, 1) == 201) && (unedited(i, j, 2) == 180) && (unedited(i, j, 3) == 88)
            colorsChanged(i,j,:) = [75,63,12];
        end
    end
end
squaresHighlighted = bwareaopen(squaresHighlighted, 100);
figure, imshow(squaresHighlighted)
figure, imshow(colorsChanged)