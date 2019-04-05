import os
from conans import ConanFile, CMake, tools


class LibrealsenseConan(ConanFile):
    name = "librealsense"
    version = "2.19.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Librealsense here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    source_subfolder = "librealsense-{version}".format(version=version)

    def source(self):
        url = "https://github.com/IntelRealSense/librealsense/archive/v{version}.zip".format(version=self.version)
        tools.get(url)

        insert_position = "project(librealsense2 LANGUAGES CXX C)"
        tools.replace_in_file(os.path.join(self.source_subfolder, "CMakeLists.txt"),
            insert_position, insert_position + '''
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def configure_cmake(self):
        cmake = CMake(self)
        if self.settings.compiler == "Visual Studio":
            cmake.definitions["BUILD_WITH_STATIC_CRT"] = "MT" in str(self.settings.compiler.runtime)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_folder=self.source_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
        if not self.options.shared:
            self.copy("*.lib", dst="lib", src="libusb_install", keep_path=False)

    def package_info(self):
        libs = ["realsense2"]
        if not self.options.shared:
            libs.extend(["realsense-file", "tm", "usb"])
        self.cpp_info.libs = libs

