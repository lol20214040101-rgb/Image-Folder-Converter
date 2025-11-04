import os
import shutil
import subprocess
import sys
from PIL import Image
import configparser
import time

# Fix console encoding for proper emoji display
if os.name == 'nt':  # Windows
    try:
        # Set console to UTF-8
        subprocess.run(['chcp', '65001'], shell=True, capture_output=True)
        os.system('cls')  # Clear screen after changing encoding
    except:
        pass

def print_banner():
    """Print a cool ASCII banner with proper emoji support 🎨"""
    # Try to enable emoji support
    try:
        # Test emoji display
        test_emoji = "🎨"
        print(test_emoji, end="", flush=True)
        print("\r", end="")  # Clear test
        emoji_support = True
    except:
        emoji_support = False
    
    if emoji_support:
        banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║  🎨 FOLDER ICON CONVERTER 2025 🚀                            ║
    ║  ════════════════════════════════════════════════════════    ║
    ║  📸 Convert Images → 🗂️  Custom Folder Icons                 ║
    ║  ✨ The Ultimate Folder Customization Tool ✨                ║
    ╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
        print("🔥 Initializing the magic... 🔥\n")
    else:
        # Fallback ASCII version without emojis
        banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║  [*] FOLDER ICON CONVERTER 2025 [*]                         ║
    ║  ════════════════════════════════════════════════════════    ║
    ║  [>] Convert Images -> Custom Folder Icons                  ║
    ║  [*] The Ultimate Folder Customization Tool [*]            ║
    ╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
        print("[!] Initializing the magic...\n")

# Global emoji support flag
EMOJI_SUPPORT = True

def safe_print(message):
    """Print message with emoji fallback support"""
    global EMOJI_SUPPORT
    
    if not EMOJI_SUPPORT:
        # Replace emojis with ASCII alternatives
        replacements = {
            '🎨': '[*]', '🚀': '[>]', '📸': '[IMG]', '🗂️': '[DIR]', '✨': '[*]',
            '🔥': '[!]', '📦': '[PKG]', '✅': '[OK]', '🎸': '[♪]', '📋': '[INFO]',
            '🔄': '[~]', '📐': '[=]', '🎉': '[!]', '📏': '[=]', '❌': '[X]',
            '🎯': '[>]', '🥷': '[H]', '🫥': '[H]', '📝': '[W]', '🛡️': '[S]',
            '🌟': '[*]', '📁': '[D]', '🔍': '[?]', '💥': '[!]', '🧹': '[C]',
            '🎊': '[*]', '🎭': '[M]', '🔧': '[T]', '💡': '[i]', '🎮': '[>]',
            '⚡': '[!]', '👋': '[~]', '📍': '[>]', '😔': '[:(]', '⠋': '[|]',
            '⠙': '[/]', '⠹': '[-]', '⠸': '[\\]', '⠼': '[|]', '⠴': '[/]',
            '⠦': '[-]', '⠧': '[\\]', '⠇': '[|]', '⠏': '[/]'
        }
        
        for emoji, replacement in replacements.items():
            message = message.replace(emoji, replacement)
    
    try:
        print(message, flush=True)
    except UnicodeEncodeError:
        # Final fallback - remove all non-ASCII characters
        ascii_message = ''.join(char if ord(char) < 128 else '?' for char in message)
        print(ascii_message, flush=True)
    """Install required packages with style 📦"""
    try:
        import PIL
        from PIL import Image
        print("✅ Pillow library found! Ready to rock! 🎸")
        
        # Check Pillow version
        pil_version = PIL.__version__
        print(f"📋 Pillow version: {pil_version}")
        
    except ImportError:
        print("📦 Installing Pillow library...")
        print("🔄 This might take a moment, grab some coffee ☕")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow>=8.0.0"])
        print("✨ Installation complete! Let's go! 🚀")
        import PIL

def install_required_packages():
    """Install required packages with style 📦"""
    global EMOJI_SUPPORT
    try:
        import PIL
        from PIL import Image
        safe_print("✅ Pillow library found! Ready to rock! 🎸")
        
        # Check Pillow version
        pil_version = PIL.__version__
        safe_print(f"📋 Pillow version: {pil_version}")
        
    except ImportError:
        safe_print("📦 Installing Pillow library...")
        safe_print("🔄 This might take a moment, grab some coffee ☕")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow>=8.0.0"])
        safe_print("✨ Installation complete! Let's go! 🚀")
        import PIL

def convert_to_ico(image_path, output_path):
    """Convert image to .ico format properly for Windows folder icons 🖼️➡️📂"""
    try:
        safe_print(f"🔄 Converting: {os.path.basename(image_path)}")
        
        with Image.open(image_path) as img:
            # Get original dimensions
            original_width, original_height = img.size
            safe_print(f"📐 Original size: {original_width}x{original_height}")
            
            # Convert to RGBA for proper transparency support
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Create proper icon sizes for Windows compatibility
            # Windows expects specific sizes for folder icons
            icon_sizes = []
            
            # Add original size if it's reasonable (max 256x256 for best compatibility)
            if original_width <= 256 and original_height <= 256:
                icon_sizes.append((original_width, original_height))
            else:
                # Scale down maintaining aspect ratio
                if original_width > original_height:
                    new_width = 256
                    new_height = int(original_height * 256 / original_width)
                else:
                    new_height = 256
                    new_width = int(original_width * 256 / original_height)
                icon_sizes.append((new_width, new_height))
            
            # Add standard Windows icon sizes for better compatibility
            standard_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128)]
            for size in standard_sizes:
                if size not in icon_sizes:
                    icon_sizes.append(size)
            
            # Create images for each size
            images = []
            for width, height in icon_sizes:
                resized = img.resize((width, height), Image.Resampling.LANCZOS)
                # Ensure proper color mode
                if resized.mode != 'RGBA':
                    resized = resized.convert('RGBA')
                images.append(resized)
            
            # Save as proper .ico file with multiple sizes
            images[0].save(
                output_path, 
                format='ICO', 
                sizes=[(img.width, img.height) for img in images],
                bitmap_format='png'  # Use PNG compression for better quality
            )
            
            safe_print(f"✅ Successfully converted to Windows-compatible .ico! 🎉")
            safe_print(f"📏 Created with {len(images)} size variants")
            return True
            
    except Exception as e:
        safe_print(f"❌ Error converting {image_path}: {e}")
        # Try alternative method using basic conversion
        try:
            safe_print("🔄 Trying alternative conversion method...")
            with Image.open(image_path) as img:
                # Simple conversion maintaining original size
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                
                # Resize if too large
                if img.width > 256 or img.height > 256:
                    img.thumbnail((256, 256), Image.Resampling.LANCZOS)
                
                img.save(output_path, format='ICO')
                safe_print(f"✅ Alternative conversion successful! 🎯")
                return True
        except Exception as e2:
            safe_print(f"❌ Alternative method also failed: {e2}")
            return False

def hide_file(file_path):
    """Hide file like a ninja 🥷"""
    try:
        # On Windows
        if os.name == 'nt':
            subprocess.run(['attrib', '+H', file_path], check=True, shell=True)
            safe_print(f"🫥 File hidden successfully: {os.path.basename(file_path)}")
        else:
            # On Linux/Mac - add dot prefix
            directory = os.path.dirname(file_path)
            filename = os.path.basename(file_path)
            if not filename.startswith('.'):
                new_path = os.path.join(directory, '.' + filename)
                os.rename(file_path, new_path)
                safe_print(f"🫥 File hidden successfully: .{filename}")
        return True
    except Exception as e:
        safe_print(f"❌ Error hiding file {file_path}: {e}")
        return False

def create_desktop_ini(folder_path, icon_name):
    """Create desktop.ini file for custom folder icon 📝✨"""
    desktop_ini_path = os.path.join(folder_path, 'desktop.ini')
    
    try:
        safe_print(f"📝 Creating desktop.ini for: {os.path.basename(folder_path)}")
        
        # Create desktop.ini content
        ini_content = f"""[.ShellClassInfo]
IconResource={icon_name},0
[ViewState]
Mode=
Vid=
FolderType=Generic
"""
        
        # Write the file
        with open(desktop_ini_path, 'w', encoding='utf-8') as f:
            f.write(ini_content)
        
        # Hide desktop.ini file
        hide_file(desktop_ini_path)
        
        # Make folder a system folder
        if os.name == 'nt':
            subprocess.run(['attrib', '+S', folder_path], check=True, shell=True)
            safe_print(f"🛡️  Folder marked as system folder")
        
        return True
    except Exception as e:
        safe_print(f"❌ Error creating desktop.ini: {e}")
        return False

def update_existing_desktop_ini(desktop_ini_path, new_icon_name):
    """Update existing desktop.ini file 🔄"""
    try:
        safe_print(f"🔄 Updating existing desktop.ini...")
        
        # Temporarily remove hidden attribute
        if os.name == 'nt':
            subprocess.run(['attrib', '-H', desktop_ini_path], shell=True)
        
        # Read current file
        config = configparser.ConfigParser()
        config.read(desktop_ini_path, encoding='utf-8')
        
        # Update IconResource
        if not config.has_section('.ShellClassInfo'):
            config.add_section('.ShellClassInfo')
        
        config.set('.ShellClassInfo', 'IconResource', f'{new_icon_name},0')
        
        # Write updates
        with open(desktop_ini_path, 'w', encoding='utf-8') as f:
            config.write(f, space_around_delimiters=False)
        
        # Hide file again
        hide_file(desktop_ini_path)
        safe_print(f"✅ Desktop.ini updated successfully! 🎯")
        
        return True
    except Exception as e:
        safe_print(f"❌ Error updating desktop.ini: {e}")
        return False

def animate_progress(text, duration=2):
    """Cool animated progress indicator 🌟"""
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{animation[i % len(animation)]} {text}", end="", flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r✅ {text} - Done! 🎉")

def process_images(directory_path):
    """Process all images in the specified directory 🖼️🔄"""
    # Check if directory exists
    if not os.path.exists(directory_path):
        print(f"❌ Directory {directory_path} does not exist!")
        return
    
    print(f"📁 Processing directory: {directory_path}")
    print("🔍 Scanning for images...")
    
    # Supported image formats
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp', '.ico']
    
    # Find all images
    image_files = []
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in supported_formats:
                image_files.append(file)
    
    print(f"🎯 Found {len(image_files)} image files! Let's process them! 🚀")
    print("=" * 60)
    
    if not image_files:
        print("😔 No image files found in the directory.")
        return
    
    # Convert all images to .ico
    ico_files = []
    print("🔄 Phase 1: Converting images to .ico format...")
    
    for i, image_file in enumerate(image_files):
        file_path = os.path.join(directory_path, image_file)
        file_name = os.path.splitext(image_file)[0]
        file_ext = os.path.splitext(image_file)[1].lower()
        
        print(f"📸 [{i+1}/{len(image_files)}] Processing: {image_file}")
        
        if file_ext != '.ico':
            # Convert to .ico
            ico_path = os.path.join(directory_path, f"{file_name}.ico")
            if convert_to_ico(file_path, ico_path):
                ico_files.append(f"{file_name}.ico")
                print(f"🎨 Converted: {image_file} ➡️  {file_name}.ico")
            else:
                print(f"💥 Failed to convert: {image_file}")
        else:
            ico_files.append(image_file)
            print(f"✅ Already .ico format: {image_file}")
    
    print("\n🗑️  Phase 2: Cleaning up non-.ico files...")
    
    # Delete non-.ico files
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in supported_formats and file_ext != '.ico':
                try:
                    os.remove(file_path)
                    print(f"🗑️  Deleted: {file}")
                except Exception as e:
                    print(f"❌ Error deleting {file}: {e}")
    
    print(f"\n📂 Phase 3: Creating custom folders and applying icons...")
    print("🎨 This is where the magic happens! ✨")
    
    # Create folders and apply icons
    for i, ico_file in enumerate(ico_files):
        ico_path = os.path.join(directory_path, ico_file)
        if os.path.exists(ico_path):
            # Folder name (without .ico extension)
            folder_name = os.path.splitext(ico_file)[0]
            folder_path = os.path.join(directory_path, folder_name)
            
            print(f"\n🎯 [{i+1}/{len(ico_files)}] Setting up folder: {folder_name}")
            
            # Create folder
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"📁 Created folder: {folder_name}")
            else:
                print(f"📁 Folder already exists: {folder_name}")
            
            # Copy .ico file to folder
            destination_ico = os.path.join(folder_path, ico_file)
            shutil.copy2(ico_path, destination_ico)
            print(f"📋 Copied original-size icon to folder")
            
            # Hide .ico file inside folder
            hide_file(destination_ico)
            
            # Create or update desktop.ini
            desktop_ini_path = os.path.join(folder_path, 'desktop.ini')
            if os.path.exists(desktop_ini_path):
                update_existing_desktop_ini(desktop_ini_path, ico_file)
            else:
                create_desktop_ini(folder_path, ico_file)
            
            # Delete original .ico file from main directory
            try:
                os.remove(ico_path)
                print(f"🧹 Cleaned up original icon file")
            except Exception as e:
                print(f"❌ Error deleting original {ico_file}: {e}")
            
            print(f"✨ Folder '{folder_name}' is now ready with custom icon! 🎊")

def main():
    """Main function - Let's start the magic! 🎭"""
    print_banner()
    
    # Install required packages
    print("🔧 Checking dependencies...")
    install_required_packages()
    
    print("\n" + "=" * 60)
    print("🎯 READY TO TRANSFORM YOUR FOLDERS! 🎯")
    print("=" * 60)
    
    # Get directory path from user
    print("📍 Please enter the directory path containing your images:")
    print("💡 Tip: You can drag and drop the folder here, or just press Enter for current directory")
    directory = input("🗂️  Directory path: ").strip()
    
    # Use current directory if no path entered
    if not directory:
        directory = os.getcwd()
        print(f"📁 Using current directory: {directory}")
    
    # Clean path
    directory = directory.strip('"')  # Remove quotes if present
    
    print(f"\n🚀 Starting the transformation process...")
    print(f"📍 Target directory: {directory}")
    print("=" * 60)
    
    # Process images
    animate_progress("Initializing magic", 1)
    process_images(directory)
    
    print("\n" + "=" * 60)
    print("🎉 MISSION ACCOMPLISHED! 🎉")
    print("✨ Your folders now have awesome custom icons! ✨")
    print("🔄 You might need to refresh your file explorer to see the changes")
    print("=" * 60)
    
    input("\n🎮 Press Enter to exit the awesome tool... ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚡ Process interrupted by user! Goodbye! 👋")
    except Exception as e:
        print(f"\n💥 Unexpected error occurred: {e}")
        input("Press Enter to exit...")
