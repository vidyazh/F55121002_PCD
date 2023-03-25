img = imread('tangled_hsv.png');

% Ekstraksi komponen R, G, B dari gambar
R = img(:,:,1);
G = img(:,:,2);
B = img(:,:,3);

% Normalisasi R, G, B ke [0, 1]
R = double(R)/255;
G = double(G)/255;
B = double(B)/255;

% Inisialisasi matriks H, S, V dengan nol
H = zeros(size(img,1),size(img,2));
S = zeros(size(img,1),size(img,2));
V = zeros(size(img,1),size(img,2));

% Konversi gambar dari RGB ke HSV
for i = 1:size(img,1)
    for j = 1:size(img,2)
        [H(i,j), S(i,j), V(i,j)] = rgb2hsv([R(i,j), G(i,j), B(i,j)]);
    end
end

% Normalisasi SV ke [0, 1] dan H ke [0, 360]
H = double(H);
S = double(S);
V = double(V);

if max(max(H)) > 1.0 || max(max(S)) > 1.0  || ...
   max(max(V)) > 1.0
    H = H / 255 * 360;
    S = S / 255;
    V = V / 255;
end

% Konversi gambar dari HSV ke RGB
R = zeros(size(img,1),size(img,2));
G = zeros(size(img,1),size(img,2));
B = zeros(size(img,1),size(img,2));

for m=1:size(img,1)
    for n=1:size(img,2)
        if S(m,n) == 0
            R(m,n) = V(m,n);
            G(m,n) = V(m,n);
            B(m,n) = V(m,n);
        else
            % S != 0

            % Menghitung posisi sektor (0 s/d 5)
            H(m,n) = H(m,n) / 60;
            sektor = floor(H(m,n)); 
            faktor = H(m,n) - sektor;
            p = V(m,n) * (1 - S(m,n));
            q = V(m,n) * (1 - S(m,n) * faktor);
            t = V(m,n) * (1 - S(m,n) * (1 - faktor));

            switch sektor
                case 0
                    R(m,n) = V(m,n);
                    G(m,n) = t;
                    B(m,n) = p;
                case 1
                    R(m,n) = q;
                    G(m,n) = V(m,n);
                    B(m,n) = p;
                case 2
                    R(m,n) = p;
                    G(m,n) = V(m,n);
                    B(m,n) = t;
                case 3
                    R(m,n) = p;
                    G(m,n) = q;
                    B(m,n) = V(m,n);
                case 4
                    R(m,n) = t;
                    G(m,n) = p;
                    B(m,n) = V(m,n);
                otherwise % sektor 5 atau 6
                    R(m,n) = V(m,n);
                    G(m,n) = p;
                    B(m,n) = q;
            end
        end
    end
end

% Normalisasi channel RGB
R = uint8(R * 255);
G = uint8(G * 255);
B = uint8(B * 255);

% Kombinasi channel dan tampilkan hasil
RGB = cat(3, R, G, B);
imshow(RGB);
imwrite(RGB, 'hasil_rgb.png');

