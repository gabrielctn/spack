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
    version("0.1.38", tag="v1.0.38", commit="d7189bfbb82a92a8e0cf3e0bd1a313c5f8c56b9d")
    version("0.1.37", sha256="2fabcbb697a92f3baffabdb28683864983663a0a4dd7fe91018fad693065ba85")
    version("0.1.36a", sha256="9eefaa0afd9be73527841cf7f061fb0392ea7866b1792a216495371fb4f2692b")
    version("0.1.36", sha256="3a1af7580767ca06b1c59e2ce33546f485f0f15b396f5cff35dfaee83fc0847c")
    version("0.1.35", sha256="52466e4c7476d250649d99b020e13bacaeab513269258a4fd9e423444071b6fd")
    version("0.1.34", sha256="572680c0f04c7498d6ac779fc6ad911db29f2b544c43716f8b8fa6924a686a4e")
    version("0.1.33", sha256="1e77bee4839096250943abe16e62364ec184d414c5b1e583d5ea749a1d0f0c9b")
    version("0.1.32", sha256="88171418fa24c10198c73d67c9f15ef95bbc506c58ceb4b8c3edcf6e0e98880e")
    version("0.1.31", sha256="04d10fc935b2b3dcf2eb0583761be523b58caac6c968fc2d2e3080a329081380")
    version("0.1.30", sha256="eb9cac4a2023450616d3f49b4133543f3b576ea6ed76a6652a0fd1bdd0ccb218")
    version("0.1.22", sha256="c082dd0deefa44d26f74044bad6a1946bb668f7f25c55fdd0b761d89f9a3250f")
    version("0.1.25", tag="v0.1.25", commit="8875737f85d43186f220e3fabdeb3a8f59ad6d08")
    version("0.1.24", tag="v0.1.24", commit="091a25ccc0137a927da8603b649a18f9761b92fa")
    version("0.1.22", tag="v0.1.22", commit="ed9a018999db04193f30d9714cfb3e6385b6d577")

    variant("shared", default=True, description="Build static or shared libraries")

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
