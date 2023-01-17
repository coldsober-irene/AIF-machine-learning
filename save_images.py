import cv2, time
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
                    cv2.imwrite(f"images//image{self.frames}.png", frame)
                    # INCREMENT IMAGES SAVED
                    self.img_saved += 1
            else:
                if keyboard_key_pressed == ord(self.manual_save_key):
                    cv2.imwrite(f"images//image{self.frames}.png", frame)
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
    

camera = capture_img(img_per_time = 4, time = 5, num_img_to_stop_at = 7)
camera.time_report()
