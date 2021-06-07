# yle-dl package for Fedora

[yle-dl](https://github.com/aajanki/yle-dl/) is a tool for downloading media files from the video streaming services of the Finnish national broadcasting company Yle: Yle Areena, Elävä Arkisto and Yle news.

This repository is used to generate the Copr repo [teervo/yle-dl](https://copr.fedorainfracloud.org/coprs/teervo/yle-dl/).

To install, first enable the repository
```
sudo dnf copr enable teervo/yle-dl
```

The package depends on `ffmpeg`, which is on Fedora is provided by the [RPM Fusion](https://rpmfusion.org/) repository. If you don't yet have the repo enabled, do so by running
```
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm 
```

To install `yle-dl`, run
```
sudo dnf install yle-dl
```
