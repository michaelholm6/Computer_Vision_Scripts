clear
unedited = imread('Real_test_3.jpg');
figure, imshow(unedited)
edited = unedited;
%Smoothing colors for telling what color each box is for the numbers at the
%end
test2 = imgaussfilt(unedited, 10);
figure, imshow(test2)
%Making yellow darker to binarize it easier without binarizing the noise
for i = 1:size(edited, 1)
         for j = 1:size(edited, 2)
            if edited(i, j, 1) > 100 && edited(i, j, 3) < 180
                 edited(i, j, :) = [0, 0, 0];
             end
         end
end

words = ['!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0];
letters = ['B' 'S' 'Q' 'A','E', 'G','D' 'O' 'N', 'R', 'P', 'M' 'K', 'U', 'W', 'X', 'Z', 'F', 'C','T', 'Y' 'L' 'H' 'I', 'V', 'J'];
for letter = 1:26
    filePath = append(letters(letter), '.png');
    seLetter = imread(filePath);
     originalEdited = edited;
     binary = imbinarize(edited, .7);
     binary = ~binary(:,:,1);
     binary = bwareaopen(binary, 10);
     binary = imerode(binary, strel('rectangle', [3 3]));
     binary = ~binary;
     binary = bwareafilt(binary, [0, 1000000]);
    se = imbinarize(seLetter, .9);
    se = se(:,:,1);
    %Cropping input image
    topCoordinate = inf;
    bottomCoordinate = 0;
    leftCoordinate = inf;
    rightCoordinate = 0;
    sizeImage = [size(se, 1), size(se, 2)];
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if se(i, j) == 0 && i < topCoordinate
                topCoordinate = i;
            end
            if se(i, j) == 0 && i > bottomCoordinate
                bottomCoordinate = i;
            end
            if se(i, j) == 0 && j < leftCoordinate
                leftCoordinate = j;
            end
            if se(i, j) == 0 && j > rightCoordinate
                rightCoordinate = j;
            end
        end
    end

    cropRectangle = [leftCoordinate, topCoordinate, rightCoordinate-leftCoordinate bottomCoordinate-topCoordinate];
    seCropped = imcrop(se, cropRectangle);
    seCropped = seCropped(5:size(seCropped, 1)-5,5:size(seCropped, 2)-5);
    %Scaling structure elements to fit them to whatever size the input
    %image is
    sizeImage = [size(seCropped, 1), size(seCropped, 2)];
    sizeImageBinary = [size(binary, 1), size(binary, 2)];
    sizeFactor = (sizeImageBinary(1)/7.2)/(sizeImage(1));
    se = seCropped;
    se = ~se(:,:,1);
    %Eroding structure elements to fit them in the letters without being
    %too lenient
    se = imerode(se, strel('rectangle', [4 4]));
    se = imresize(se, sizeFactor);
    se = imerode(se, strel('rectangle', [7 7]));
    eroded = imerode(binary, se);
    sizeImage = [size(eroded, 1), size(eroded, 2)];
    %Putting letters into final strings and checking colors of their
    %related boxes
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if eroded(i, j) == 1
                word = ceil((i)/((sizeImage(1)/6)));
                position = ceil((j)/(sizeImage(2)/5));
                if words(word, position) == '!' && i-90>0 && j-90 > 0
                    words(word, position) = letters(letter);
                    if test2(i-70, j-70, 1) > 150 && test2(i-90, j-90, 3) < 90
                        words(word, 7) = words(word, 7) + 1;
                    elseif test2(i-100, j-100, 1) < 110 && test2(i-100, j-100, 2) > 110
                        words(word, 6) = words(word, 6) + 1;
                    end
                end
            end
        end
    end
end

for i=1:size(words, 1)
    if words(i, 1) ~= '!'
        string = append(words(i, 1:5),' ', int2str(words(i, 6)),' ', int2str(words(i, 7)));
        disp(string)
    end
end

% If I had more time to work on this program, I would improve it several
% ways. First of all, I'd make it faster. This takes a LONG time to run (2+
% minutes). I'd make it faster by downsampling the image at the beginning.
% I'd also make it so this program can more easily crop the image itself,
% even if a sub-optimal image is provided. I would also make it so the
% program only looks for letters in the sections of the image where letters
% probably are. This program does not need to check for letter in the far
% upper left hand corner of the image. Also, if I ahd more time, I would
% use a more robust system for detecting the square colors. I would also
% try to create a more accurate character detection system.
%
%Some challenges I encountered included scaling the image and letter
%templates to have the same size, so the templates were able to line up
%with the letters. I also struggled with detecting the color of the input
%image boxes, because there was some noise in the image due to the frame
%rate of my monitor. I solved this by blurring the image. 