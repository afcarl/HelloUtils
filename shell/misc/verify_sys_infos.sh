# http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#pre-installation-actions

# Verify You Have a CUDA-Capable GPU
echo -e "Verify CUDA-Capable GPU:"
echo -e "###############################################"
lspci | grep -i nvidia
echo -e "###############################################\n"

# Verify You Have a Supported Version of Linux
echo -e "Verify Linux version:"
echo -e "###############################################"
uname -m && cat /etc/*release
echo -e "###############################################\n"

# Verify the System Has gcc Installed
echo -e "Verify GCC version:"
echo -e "###############################################"
gcc --version | grep gcc
echo -e "###############################################\n"

# Verify the System has the Correct Kernel Headers and Development Packages Installed
echo -e "Verify kernel headers & development packages:"
echo -e "###############################################"
uname -r
echo -e "###############################################\n"

# Check GLIBC version
echo -e "Check GLIBC version:"
echo -e "###############################################"
ldd --version | grep ldd
echo -e "###############################################\n"
