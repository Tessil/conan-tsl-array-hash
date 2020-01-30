from conans import ConanFile, CMake, tools
import os

class TslArrayHashConan(ConanFile):
    name = "tsl-array-hash"
    version = "0.7.0"
    license = "MIT"
    description = "C++ implementation of a fast and memory efficient hash map and hash set specialized for strings."
    homepage = "https://github.com/Tessil/array-hash"
    url = "https://github.com/Tessil/conan-tsl-array-hash"
    exports = "LICENSE"

    def source(self):
        tools.get("%s/archive/v%s.tar.gz" % (self.homepage, self.version))

    def package(self):
        self.copy("LICENSE", dst="licenses", keep_path=False, ignore_case=True)
        
        cmake = CMake(self)
        cmake.configure(source_folder="array-hash-%s" % (self.version))
        cmake.install()

    def package_id(self):
        self.info.header_only()
