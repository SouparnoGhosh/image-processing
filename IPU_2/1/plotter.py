import matplotlib.pyplot as plt
import cv2
import inspect
import warnings
import matplotlib.cbook

# warnings.filterwarnings("ignore", category=matplotlib.cbook.MatplotlibDeprecationWarning)


def custom_plot(*args, rows=2, cols=3, grayscale=False):
    num_images = len(args)

    plt.figure(figsize=(19, 7))
    plt.tight_layout()
    # plt.subplots_adjust(wspace=0, hspace=0)
    # plt.axis("off")

    frame = inspect.currentframe()
    local_vars = frame.f_back.f_locals
    for i in range(num_images):
        # plt.subplot(
        #     ((num_images // 3.1) + 1),
        #     (((num_images - 1) % 3) + 1) if num_images <= 3 else 3,
        #     i + 1,
        # )
        ax = plt.subplot(rows, cols, i + 1)
        # Turn off tick labels
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        # plt.imshow(cv2.cvtColor(args[i], cv2.COLOR_BGR2RGB))
        (plt.imshow(args[i], cmap="gray") if grayscale else plt.imshow(cv2.cvtColor(args[i], cv2.COLOR_BGR2RGB)))
        title = [name for name, var in local_vars.items() if var is args[i]][0]
        plt.title(title)

    # Display the plot
    plt.show()
