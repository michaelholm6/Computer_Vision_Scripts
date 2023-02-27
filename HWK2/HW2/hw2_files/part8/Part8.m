clear
unedited = imread('image_part8a.png');
figure, imshow(unedited)
edited = unedited;
words = ['!' '!' '!' '!' '!';'!' '!' '!' '!' '!';'!' '!' '!' '!' '!';'!' '!' '!' '!' '!';'!' '!' '!' '!' '!';'!' '!' '!' '!' '!'];
letters = ['A','B','D','E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'C', 'I'];
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
    binary = imbinarize(edited, .999999);
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
    binary = imcrop(binary, cropRectangle);
    binary = bwareafilt(binary, [0,1000]);
    se = imbinarize(seLetter, .9);
    se = ~se(:,:,1);
    eroded = imerode(binary, se);
    eroded = bwareafilt(eroded, [0,2]);
    sizeImage = [size(eroded, 1), size(eroded, 2)];
    %Adding letters to output strings
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if eroded(i, j) == 1
                word = ceil((i)/68);
                position = ceil((j)/68);
                if words(word, position) == '!'
                    words(word, position) = letters(letter);
                end
            end
        end
    end
end

for i=1:size(words, 1)
    if words(i, 1) ~= '!'
        disp(words(i, :))
    end
end