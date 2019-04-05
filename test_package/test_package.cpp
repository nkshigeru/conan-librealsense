#include <iostream>
#include <librealsense2/rs.hpp>

int main() {
    std::cout << "Compiled with librealsense " << RS2_API_VERSION_STR
        << " (" << RS2_API_VERSION << ")" << std::endl;
    std::cout << "Using " << rs2_get_api_version(NULL) << std::endl;
}
