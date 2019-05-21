name:       TestPractice
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%pre
echo "installing-------package"
echo "-------------------------"

%build
touch new.bin

%install	
mkdir -p %{buildroot}/opt/test
install -m 755 new.bin %{buildroot}/opt/test/new.bin


%files
/opt/test/

%post
chown -R root:root /opt/test/new.bin
chmod -R 755 /opt/test/ 

echo "completed"
