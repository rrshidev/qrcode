import os
import shutil
import qrcode
import random
import json
import PIL


def generate_qr_codes(n, uri_root, min_range, max_range, output_dir):
    random_ids = []
    while len(random_ids) != n:
        random_id = random.randint(min_range, max_range)
        if random_id not in random_ids:
            random_ids.append(random_id)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    img_dir = 'qr_codes'
    if not os.path.exists('{}/{}'.format(output_dir, img_dir)):
        os.makedirs('{}/{}'.format(output_dir, img_dir))

    cnt = 0
    qr_codes = []
    for random_id in random_ids:
        cnt += 1
        qr.add_data(uri_root + str(random_id))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((3000, 3000))
        filepath = '{}/qr_{}.png'.format(img_dir, cnt)
        img.save('{}/{}'.format(output_dir, filepath))
        qr.clear()
        qr_codes.append({'id': random_id, 'filepath': filepath})

    with open('{}/index.json'.format(output_dir), "w") as write_file:
        json.dump(qr_codes, write_file)

    shutil.make_archive('output', 'zip', output_dir)


count_link = int(input('Enter the required number of qrcodes: '))
print(generate_qr_codes(count_link, 'https://trace.top/', 10000000, 99999999, 'output'))



dfdfd