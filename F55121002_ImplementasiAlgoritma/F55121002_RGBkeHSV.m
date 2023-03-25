img = imread('tangled.png');

% Pisahkan masing-masing channel warna RGB dari gambar
R = img(:,:,1);
G = img(:,:,2);
B = img(:,:,3);

% Lakukan normalisasi RGB ke dalam jangkauan [0, 1]
R = double(R)/255;
G = double(G)/255;
B = double(B)/255;

% Buat matriks kosong untuk menyimpan hasil konversi ke format HSV
H = zeros(size(img,1),size(img,2));
S = zeros(size(img,1),size(img,2));
V = zeros(size(img,1),size(img,2));

% Hitung nilai H, S, dan V untuk setiap piksel
for m=1: size(img,1)
    for n=1: size(img,2)
        minrgb = min([R(m,n) G(m,n) B(m,n)]); 
        maxrgb = max([R(m,n) G(m,n) B(m,n)]); 
        V(m,n) = maxrgb;
        delta = maxrgb - minrgb;
        
        if maxrgb == 0
            S(m,n) = 0;
        else
            S(m,n) = 1 - minrgb / maxrgb;
        end
    
        if S(m,n) == 0
            H(m,n) = 0;
        else
            SV = S(m,n) * V(m,n);
        
            if R(m,n) == maxrgb
                % Di antara kuning dan magenta
                H(m,n) = (G(m,n)-B(m,n)) / SV;
            elseif G(m,n) == maxrgb
                % Di antara cyan dan kuning
                H(m,n) = 2 + (B(m,n)-R(m,n)) / SV;
            else
                % Di antara magenta dan cyan
                H(m,n) = 4 + (R(m,n)-G(m,n)) / SV;
            end
            
            H(m,n) = H(m,n) * 60;
            if H(m,n) < 0
                H(m,n) = H(m,n)+360;
            end
        end
    end
end

% Konversikan nilai H, S, dan V ke dalam jangkauan [0, 255]
H = uint8(H * 255/360);
S = uint8(S * 255);
V = uint8(V * 255);

% Gabungkan matriks H, S, dan V menjadi satu gambar HSV
hsv_img = cat(3, H, S, V);

% Tampilkan gambar HSV
imshow(hsv_img);
