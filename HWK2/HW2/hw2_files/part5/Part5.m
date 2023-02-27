clear
unedited = imread('image_part5a.png');
edited = unedited;
vowels = ['A','E','I','O','U', 'Y'];
colors = [255 0 0; 0 255 0; 0 0 255;0 255 255; 255 255 0; 100 100 100];
for vowel = 1:size(vowels, 2)
    filePath = append('../../letter_cutouts/', vowels(vowel), '.png');
    seLetter = imread(filePath);
    binary = imbinarize(edited, .999999);
    binary = ~binary(:,:,1);
    se = imbinarize(seLetter, .9);
    se = se(:,:,1);
    eroded = imerode(binary, se);
    eroded = bwareafilt(eroded, [0,1]);
    se = imbinarize(seLetter, .65);
    eroded = imdilate(eroded, se);
    eroded = ~eroded;
    eroded = ~bwareafilt(eroded, [0,100000]);
    sizeImage = [size(eroded, 1), size(eroded, 2)];
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if eroded(i, j) == 0
                edited(i,j,:) = colors(vowel, :);
            end
        end
    end
end
figure, imshow(edited)