import cv2
from playwright.sync_api import sync_playwright


def find_image_coordinates(screenshot_path, target_path, threshold=0.8):
    screenshot = cv2.imread(screenshot_path, 0)
    target = cv2.imread(target_path, 0)

    result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # top-left corner of match
        top_left = max_loc
        h, w = target.shape

        # for debugging
        # end_point = (top_left[0] + w, top_left[1] + h)
        # screenshot = cv2.rectangle(screenshot, top_left, end_point, (0, 0, 255), 2)
        # cv2.imwrite("debug.png", screenshot)

        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        print(f"Found {target_path} at: ({center_x}, {center_y})")
        return center_x, center_y
    else:
        return None


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto("https://www.online-calculator.com//html5/simple/index.php")
        page.locator("#canvas").wait_for()
        screenshot_path = "input/base.png"
        page.screenshot(path=screenshot_path)

        x_label_5, y_label_5 = find_image_coordinates(
            screenshot_path, "input/label_5.png"
        )
        page.mouse.click(x_label_5, y_label_5)
        page.wait_for_timeout(300)
        x_label_plus, y_label_plus = find_image_coordinates(
            screenshot_path, "input/label_plus.png"
        )
        page.mouse.click(x_label_plus, y_label_plus)
        page.wait_for_timeout(300)
        x_label_0, y_label_0 = find_image_coordinates(
            screenshot_path, "input/label_0.png"
        )
        page.mouse.click(x_label_0, y_label_0)
        page.wait_for_timeout(300)
        x_label_equal, y_label_equal = find_image_coordinates(
            screenshot_path, "input/label_equal.png"
        )
        page.mouse.click(x_label_equal, y_label_equal)
        page.wait_for_timeout(300)
        browser.close()


if __name__ == "__main__":
    main()
