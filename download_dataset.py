
import gdown
def download_ccpd():
    url = "https://drive.google.com/uc?id=1rdEsCUcIUaYOVRkx5IMTRNA7PcGMmSgc"
    dsetname = "CCPD2019.tar.xz"
    gdown.download(url, dsetname, quiet=False)


if __name__ == "__main__":
    download_ccpd()