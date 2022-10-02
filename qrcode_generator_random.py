import qrcode
import random

def linkGen(n):

    random_nums = []
    while len(random_nums) != n:
        qr_num = random.randint(10000000, 99999999)
        if qr_num not in random_nums:
            random_nums.append(qr_num)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    link = 'https://trace.top/'
    cnt = 0
    for random_num in random_nums:
        cnt += 1
        qr.add_data(link + str(random_num))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save('qr' + str(cnt) + '.jpg', 'JPEG')


count_link = int(input('Enter the required number of qrcodes: '))
print(linkGen(count_link))