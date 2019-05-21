name:       TestPractice
Version:    2
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%pre
echo "installing-------package"
echo "-------------------------"

%patch0
cd /opt/test
mv new.bin new1.bin

%build
touch new1.bin

%install	
mkdir -p %{buildroot}/opt/test
install -m 755 new1.bin %{buildroot}/opt/test/new1.bin


%files
/opt/test/

%post
chown -R root:root /opt/test/new1.bin
chmod -R 755 /opt/test/ 

echo "completed"
