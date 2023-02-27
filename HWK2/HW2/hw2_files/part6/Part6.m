clear
unedited = imread('image_part6a.png');
imshow(unedited)
edited = unedited;
imwrite(edited, 'part6_edited.png' );
vowels = ['A','E','I','O','U', 'Y'];
fh = figure;
imshow(edited);
for vowel = 1:size(vowels, 2)
    edited = imread('part6_edited.png');
    filePath = append('../../letter_cutouts/', vowels(vowel), '.png');
    seLetter = imread(filePath);
    binary = imbinarize(edited, .999999);
    binary = ~binary(:,:,1);
    se = imbinarize(seLetter, .9);
    se = se(:,:,1);
    eroded = imerode(binary, se);
    eroded = bwareafilt(eroded, [0,1]);
    sizeImage = [size(eroded, 1), size(eroded, 2)];
    for i=1:sizeImage(1)
        for j = 1:sizeImage(2)
            if eroded(i, j) == 1
                color = unedited(i-25, j-22,:);
                bottomLeft = [i - 25 , j - 25];
                hold on
                rectangle('FaceColor', color, 'EdgeColor', color, 'position', [bottomLeft(2), bottomLeft(1), 48, 48])
                text(j, i, vowels(vowel), 'FontName', 'Algerian', 'HorizontalAlignment','center')
            end
        end
    end
end
frm = getframe( fh );
imwrite( frm.cdata, 'images/images/part5_edited.png' );
result = imread('images/images/part5_edited.png');
hold off
close
figure, imshow(result)