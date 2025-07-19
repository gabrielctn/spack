# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.pkg.builtin.boost import Boost

class Dssp(CMakePackage):
    """'mkdssp' utility. (dictionary of protein secondary structure)"""

    homepage = "https://github.com/PDB-REDO/dssp"
    url      = "https://github.com/PDB-REDO/dssp/archive/refs/tags/v4.5.0.tar.gz"

    # New CMake-based build:
    version("4.5.0", sha256="d8cb1b3b173cb176f19b67459ad37fee203fb942951d2284dd4e8130a76f471d")

    # Build dependencies
    depends_on("cmake@3.13:", type="build")
    depends_on("boost@1.48:")
    depends_on(Boost.with_default_variants)
    depends_on("libcifpp")
    depends_on("zlib")
    depends_on("catch2", type=("build", "test"))

    # pdb data download for the built‐in test
    resource(
        name="pdb_data",
        url="https://files.rcsb.org/download/1ALK.pdb",
        sha256="99f4cd7ab63b35d64eacc85dc1491af5a03a1a0a89f2c9aadfb705c591b4b6c9",
        expand=False,
        placement="pdb",
    )

#    def cmake_args(self):
#        # Default CMakePackage will already set -DCMAKE_INSTALL_PREFIX; add
#        # any extra args here if needed.
#        args = []
#        return args

    @run_after("install")
    def cache_test_sources(self):
        """Save off the pdb sources for stand-alone testing."""
        cache_extra_test_sources(self, "pdb")

    def test_mkdssp(self):
        """Calculate structure for example."""
        pdb_path = self.test_suite.current_test_cache_dir.pdb
        mkdssp = which(self.prefix.bin.mkdssp)
        with working_dir(pdb_path):
            mkdssp("1ALK.pdb", "1alk.dssp")

    # Override the default build phases to use CMake
    # (CMakePackage does this automatically based on the class)
