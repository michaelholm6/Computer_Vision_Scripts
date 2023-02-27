clear
unedited = imread('image_part10a.png');
figure, imshow(unedited)
edited = unedited;
words = ['!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0];
letters = ['S' 'Q' 'A','B','E', 'G','D' 'O' 'N', 'R', 'P', 'M' 'K', 'U', 'W', 'W', 'X', 'Z', 'F', 'C','T', 'Y' 'L' 'H' 'I', 'V', 'J'];
for letter = 1:26
    %Removing noise in the letter templates
    filePath = append('../../letter_cutouts/', letters(letter), '.png');
    seLetter = imread(filePath);
    for i = 1:size(seLetter, 1)
        for j = 1:size(seLetter, 2)
            if seLetter(i, j, 1) ~= 0 || seLetter(i, j, 2) ~= 0 || seLetter(i, j, 3) ~= 0
                seLetter(i, j, :) = [255, 255, 255];
            end
        end
    end
    originalEdited = edited;
    binary = imbinarize(edited, .99999);
    binary = binary(:,:,1);
    topCoordinate = inf;
    bottomCoordinate = 0;
    leftCoordinate = inf;
    rightCoordinate = 0;
    %Cropping image
    sizeImage = [size(binary, 1), size(binary, 2)];
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if binary(i, j) == 0 && i < topCoordinate
                topCoordinate = i;
            end
            if binary(i, j) == 0 && i > bottomCoordinate
                bottomCoordinate = i;
            end
            if binary(i, j) == 0 && j < leftCoordinate
                leftCoordinate = j;
            end
            if binary(i, j) == 0 && j > rightCoordinate
                rightCoordinate = j;
            end
        end
    end
    cropRectangle = [leftCoordinate, topCoordinate, rightCoordinate-leftCoordinate bottomCoordinate-topCoordinate];
    originalEdited = imcrop(originalEdited, cropRectangle);
    originalEdited = imresize(originalEdited, [395, 339]);
    edited = originalEdited;
    %Removing noise that results from the crop process
    for i = 1:size(originalEdited, 1)
        for j = 1:size(originalEdited, 2)
            if (originalEdited(i, j, 1) ~= 120 || originalEdited(i, j, 2) ~= 124 || originalEdited(i, j, 3) ~= 126) && (originalEdited(i, j, 1) ~= 201 || originalEdited(i, j, 2) ~= 180 || originalEdited(i, j, 3) ~= 88) && (originalEdited(i, j, 1) ~= 106 || originalEdited(i, j, 2) ~= 170 || originalEdited(i, j, 3) ~= 100) && (originalEdited(i, j, 1) ~= 255 || originalEdited(i, j, 2) ~= 255 || originalEdited(i, j, 3) ~= 255) && (originalEdited(i, j, 1) ~= 0 || originalEdited(i, j, 2) ~= 0 || originalEdited(i, j, 3) ~= 0)
                originalEdited(i, j, :) = [255, 255, 255];
            end
        end
    end
    binary = imbinarize(originalEdited, .999999);
    binary = binary(:,:,1);
    binary = ~binary;
    binary = bwareaopen(binary, 4, 4);
    binary = ~binary;
    binary = bwareafilt(binary, [0,1000]);
    se = imbinarize(seLetter, .9);
    se = ~se(:,:,1);
    %I didnt want to make my own letter templates, so I just edited the
    %existing ones using dilate and erode operations until it worked. This
    %was through trial and error.
    if letters(letter) == 'S'
        se = imerode(se, strel('rectangle', [1 1]));
    end
     if letters(letter) == 'D'
        se = imdilate(se, strel('rectangle', [1 2]));
     end
     if letters(letter) == 'U'
        se = imdilate(se, strel('rectangle', [1 2]));
     end
     if letters(letter) == 'U'
        se = imdilate(se, strel('rectangle', [2 2]));
     end
     if letters(letter) == 'Y'
        se = imdilate(se, strel('rectangle', [3 3]));
     end
     if letters(letter) == 'L'
        se = imdilate(se, strel('rectangle', [2 2]));
     end
     if letters(letter) == 'N'
        se = imdilate(se, strel('rectangle', [3 3]));
     end
     if letters(letter) == 'C'
        se = imerode(se, strel('rectangle', [2 2]));
     end
     if letters(letter) == 'O'
        se = imdilate(se, strel('rectangle', [1 1]));
     end
    eroded = imerode(binary, se);
    sizeImage = [size(eroded, 1), size(eroded, 2)];
    %Finding color of boxes of the letters found and adding letters to
    %output strings
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if eroded(i, j) == 1
                word = ceil((i)/68);
                position = ceil((j)/68);
                if words(word, position) == '!' && i-25 >0 && j-22 > 0
                    words(word, position) = letters(letter);
                    if edited(i-20, j-20, 1) == 201 && edited(i-20, j-20, 2) == 180 && edited(i-20, j-20, 3) == 88
                        words(word, 7) = words(word, 7) + 1;
                    elseif edited(i-20, j-20, 1) == 106 && edited(i-20, j-20, 2) == 170 && edited(i-20, j-20, 3) == 100
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