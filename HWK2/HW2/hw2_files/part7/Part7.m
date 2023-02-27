clear
unedited = imread('image_part7a.png');
figure, imshow(unedited)
edited = unedited;
letters = ['A','B','D','E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'C', 'I'];
for letter = 1:26
    %Removing noise in the letter templates
    color = rand([1, 3])*255;
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
    binary = bwareafilt(binary, [0,1000]);
    se = imbinarize(seLetter, .9);
    se = ~se(:,:,1);
    eroded = imerode(binary, se);
    seLetter = imread(filePath);
    se = ~imbinarize(seLetter, .6);
    eroded = bwareafilt(eroded, [0,2]);
    eroded = imdilate(eroded, se);
    sizeImage = [size(eroded, 1), size(eroded, 2)];
    %Coloring letters
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if eroded(i, j) == 1
                edited(i,j,:) = color;
            end
        end
    end
end
figure, imshow(edited)