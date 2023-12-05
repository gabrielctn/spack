# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class Viamd(CMakePackage):
    """Visual Interactive Analysis of Molecular Dynamics"""

    homepage = "https://github.com/scanberg/viamd"
    url = "https://github.com/scanberg/viamd/archive/refs/tags/v0.1.22.tar.gz"
    git = "https://github.com/scanberg/viamd"
    submodules= True

    license("MIT")

    version("main", branch="main")
    version("0.1.25", tag="v0.1.25", commit="8875737f85d43186f220e3fabdeb3a8f59ad6d08")
    version("0.1.24", tag="v0.1.24", commit="091a25ccc0137a927da8603b649a18f9761b92fa")
    version("0.1.22", tag="v0.1.22", commit="ed9a018999db04193f30d9714cfb3e6385b6d577")

    variant("shared", default=False, description="Build static or shared libraries")

    depends_on("cmake@3.20:", type="build")
    depends_on("libx11", type=("build", "run"))
    depends_on("libxrandr", type=("build", "run"))
    depends_on("libxinerama", type=("build", "run"))
    depends_on("libxcursor", type=("build", "run"))
    depends_on("gtkplus", type=("build", "run"))
    depends_on("pkgconf", type=("build", "run"))

    def cmake_args(self):
        args = [self.define_from_variant("BUILD_SHARED_LIBS", "shared")]
        return args

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make()
            mkdirp(prefix.bin)
            mkdirp(prefix.ext)
            mkdirp(prefix.lib)
            install_tree("bin", prefix.bin)
            install_tree("ext", prefix.ext)
            install_tree("lib", prefix.lib)
