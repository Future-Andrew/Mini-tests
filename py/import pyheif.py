在git命令行下:
	1、下载vcpkg源码,并进入。
		git clone https://github.com/Microsoft/vcpkg.git
		cd vcpkg

	2、运行源码中的.sh
		./bootstrap-vcpkg.sh

	3、下载安装相关库
		（注:若下载github源码进行不下去,则可自行查看窗口下载源码的地址,自行下载后放到xxx/vcpkg/downloads文件夹下）
		./vcpkg integrate install

在doc命令下并进入vcpkg目录下:
	下载编译libheif
		./vcpkg install libheif:x64-windows
		(注:
			(编译)默认安装32位:	vcpkg install libheif 
			(编译)64位库: 		vcpkg install libheif:x64-windows
			(编译)32位库: 		vcpkg install libheif:x86-windows
		)