import argparse
import os
import cv2


def parse_args():
    parser = argparse.ArgumentParser(description="Frame extractor")

    # Params list
    parser.add_argument(
        "-p", "--path_video", type=str, default=None, help="Path to video"
    )
    parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        default="./output_frames",
        help="Path to output folder",
    )
    return parser.parse_args()


def main(args):
    videoPath = args.path_video
    outputPath = args.output_folder
    videoName = args.path_video.split("/")[-1]
    videoNameStripped = videoName.split(".")[0]
    if outputPath[-1] == "/":
        outputPath = f"{outputPath}{videoNameStripped}"
    else:
        outputPath = f"{outputPath}/{videoNameStripped}"
    print("Path to video: ", videoPath)
    print("Path to output folder: ", outputPath)
    print("Extracting frames...")
    # os.system(
    #     "ffmpeg -i {} -vf fps=1/1 {}%d.jpg".format(
    #         args.path_video, args.output_folder
    #     )
    # )
    # A video will have its own folder for ease of organization
    try:
        video = cv2.VideoCapture(videoPath)
        if not os.path.exists(outputPath):
            try:
                os.makedirs(outputPath)
            except OSError:
                print("Error: Output path does not exist and cannot be created!")
        frameNo = 1
        ret, frame = video.read()
        while ret:
            name = f"{outputPath}/frame" + str(frameNo) + ".png"
            # print("Creating..." + name)
            cv2.imwrite(name, frame)
            frameNo += 1
            ret, frame = video.read()
        video.release()
        print("Done!")
    except Exception as e:
        print("Error encountered!")
        print(e)


if __name__ == "__main__":
    args = parse_args()
    main(args)
