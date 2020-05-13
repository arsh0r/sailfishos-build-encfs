# Building encfs for SailfishOS

[Install Platform SDK](https://sailfishos.org/wiki/Platform_SDK_Installation)

[Install SDK Target](https://sailfishos.org/wiki/Platform_SDK_Target_Installation)

Install needed packages:
```
sb2 -t SailfishOS-latest-armv7hl -m sdk-install -R zypper in make automake cmake gcc gcc-c++
sb2 -t SailfishOS-latest-armv7hl -m sdk-install -R zypper in openssl-devel fuse-devel
```

Download package for encfs 1.9.5
```
curl -L -O https://github.com/vgough/encfs/releases/download/v1.9.5/encfs-1.9.5.tar.gz
tar xzf encfs-1.9.5.tar.gz
cd encfs-1.9.5
```
copy rpm directory from this repository
```
mb2 -t SailfishOS-latest-armv7hl build
```
