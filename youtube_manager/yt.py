import json


def load_data():
    try:
         with open("videos.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(videos):
    with open("videos.txt", "w") as file:
        json.dump(videos, file)

# def list_all_videos(videos):
#     for i, video in enumerate(videos, start=1):
#         print(f"{i}.Name: {video['name']}, Time: {video['time']}")

def add_videos(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data(videos)


def update_video_details(videos):
    pass


def delete_video(videos):
    pass


def main():
    videos = load_data()
    while True:
        print("\n youtube Manager | Choose an option")
        print("1.list all youtube videos")
        print("2.Add a youtube video")
        print("3.update youtube videos details")
        print("4.Delete a youtube videos")
        print("5.exsit the app")
        user_Choice = input("Enter your Choice")
        print(videos)

        match user_Choice:
            # case '1':
            #     list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_video_details(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()