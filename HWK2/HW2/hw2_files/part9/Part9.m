clear
unedited = imread('image_part9a.png');
figure, imshow(unedited)
edited = unedited;
words = ['!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0;'!' '!' '!' '!' '!' 0 0];
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
    test = imcrop(unedited, cropRectangle);
    binary = bwareafilt(binary, [0,1000]);
    se = imbinarize(seLetter, .9);
    se = ~se(:,:,1);
    eroded = imerode(binary, se);
    eroded = bwareafilt(eroded, [0,2]);
    sizeImage = [size(eroded, 1), size(eroded, 2)];
    %Finding color of boxes of the letters found and adding letters to
    %output strings
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if eroded(i, j) == 1
                word = ceil((i)/68);
                position = ceil((j)/68);
                if words(word, position) == '!'
                    words(word, position) = letters(letter);
                    if test(i-25, j-22, 1) == 201 && test(i-25, j-22, 2) == 180 && test(i-25, j-22, 3) == 88
                        words(word, 7) = words(word, 7) + 1;
                    elseif test(i-25, j-22, 1) == 106 && test(i-25, j-22, 2) == 170 && test(i-25, j-22, 3) == 100
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