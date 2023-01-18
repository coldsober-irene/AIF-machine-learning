import cv2, time
import pickle
from random import randrange
import sqlite3 as sql
import os
import json, requests

class save_img_sql:
    def __init__(self, img, image_name, time = time.strftime("%Y-%B-%d %H:%M:%S %p")) -> None:
        self.img = img
        self.filename = image_name
        self.time = time
        self.create_tb()

    def create_db(self):
        return sql.connect("cnn_images.db")
    
    def read_img(self):
        with open(self.img, 'rb') as f:
            return f.read()
        
    def create_tb(self):
        conn = self.create_db()
        with conn:
            conn.execute("CREATE TABLE IF NOT EXISTS images (image BLOB, image_name TEXT,size REAL, date TEXT)")
    
    def insert_image(self):
        row = [self.read_img(), self.filename, os.path.getsize(self.img), self.time]
        # row[0] = sql.Binary(self.read_img)
        conn = self.create_db()
        with conn:
            conn.execute("INSERT INTO images VALUES(?, ?, ?, ?)", row)
            print("Image is inserted successfully!")
    
    def retrieve_img(self):
        conn = self.create_db()
        with conn:
            fet = conn.execute("SELECT * FROM images")
            return fet.fetchone()

    def get_img(self, img_filename):
        with open(img_filename, 'wb') as f:
            f.write(self.retrieve_img()[0])
            print("Image retrieved")

class capture_img:
    image_formed = 0
    def __init__(self, img_per_time,time = 1, num_img_to_stop_at = None, stop_key = 'q', manual_save = False, manual_save_key = None) -> None:
        """time: minute"""
        self.one_time_img = img_per_time
        self.num_img_to_stop_at = num_img_to_stop_at
        self.stop_key = stop_key
        self.manual_save = manual_save
        self.manual_save_key = manual_save_key
        self.time = time 
        self.frames = 0
        self.img_saved = 0

    def is_saving_time(self):
        overall_time = self.time * 2000
        save_at = int(overall_time / self.one_time_img)
        if self.frames % save_at == 0:
            return True
        else:
            return False

    def video_capture(self):
        cap = cv2.VideoCapture(0)
        # CONTINOUS FILMING
        while True:
            ret, frame = cap.read()
            cv2.imshow("Live footage camera", frame)
            keyboard_key_pressed = cv2.waitKey(1) & 0xFF

            # SAVE THE IMAGE AUTOMATICALLY
            if not self.manual_save:
                save = self.is_saving_time()
                if save:
                    cv2.imwrite(f"images//image{randrange(0, self.img_saved+1)}.png", frame)
                    # INCREMENT IMAGES SAVED
                    self.img_saved += 1
            else:
                if keyboard_key_pressed == ord(self.manual_save_key):
                    cv2.imwrite(f"images//image{randrange(0, self.img_saved+1)}.png", frame)
                    # INCREMENT IMAGES SAVED
                    self.img_saved += 1

            # STOP FILMING
            if self.num_img_to_stop_at:
                if self.img_saved == self.num_img_to_stop_at:
                    break
            else:
                if keyboard_key_pressed == ord(self.stop_key):
                    break
            
            # INCREMENT FRAMES
            self.frames += 1
        cap.release()
        cv2.destroyAllWindows()

    def time_report(self):
        start = time.perf_counter()
        # CAPTURE IMAGES
        self.video_capture()
        # END CAPTURING IMAGES
        end = time.perf_counter()
        # DISPLAY REPORT
        print(f"{self.img_saved} images were shot in {round((end-start)/60, 1)} minutes.")
    
class increment_data:
    def __init__(self, previous_arr, new_arr) -> None:
        self.prev = previous_arr
        if ".pkl" in self.prev:
            with open(self.prev, 'rb') as f:
                self.prev = pickle.load(f)
        self.new_arr = new_arr
        if ".pkl" in self.new_arr:
            with open(self.new_arr, 'rb') as f:
                self.new_arr = pickle.load(f)
    
    def is_same_shape(self):
        prev_shape = list(self.prev.shape)
        new_shape = list(self.new.shape)
        if prev_shape == new_shape:
            return prev_shape + new_shape
        else:
            try:
                new_shape.insert(0, -1)
            except Exception:
                print("This data can't be standardized to stored one")

class upload_to_drive:
    def __init__(self, filename) -> None:
        self.file = filename
        self.route()
    
    def route(self):
        headers = {"Authorization":"Bearer ya29.a0AX9GBdUCkpXGhn0tRH_c_Ipb42XcurCai26s_Tv2WOq2Gh5ZJkiXIOU4phbZjN1Bs1T_ru_iFCfAQPiVf_C3YdPuOl0aOR0iioaga-NQtC1EIlE4EYchCESYU4Z25Hd0wXXRRP6Ns0Kw44YnGWyqe040uzPfaCgYKAYQSARESFQHUCsbCqiDYb77AFaNAeg3hoPJZQQ0163"
                    }
 
        para = {"name":os.path.basename(self.file),
                "parents":['1u3FClppCl691Gr2ryufBaQBJU-0gLxgI']}
        files = {'data':('metadata',json.dumps(para),'application/json;charset=UTF-8'),'file':open(self.file,'rb')
            }
 
        r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                            headers=headers,
                            files=files
                        )
        print("file has been uploaded successfully")

if __name__ == "__main__":
    # camera = capture_img(img_per_time = 10, time = 1, num_img_to_stop_at = 100)
    # camera.time_report()
    # base_path = "C:/Users/100050/OneDrive - AIF Rwanda/Irene Nsengumukiza/Downloads/ML/ml1/images/people"
    # img_filenames = os.listdir(base_path)
    # for img in img_filenames:
    #     db = save_img_sql(img = os.path.join(base_path, img), image_name=img)
    #     db.insert_image()
    #     db.get_img(img_filename="file_from_db.png")
    sender = upload_to_drive(filename = r"C:\Users\100050\OneDrive - AIF Rwanda\Irene Nsengumukiza\Downloads\ML\ml1\cnn_images.db")
