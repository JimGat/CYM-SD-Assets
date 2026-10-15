"""Manual SD installer must never overwrite user files or retain .example suffixes."""
from pathlib import Path
import importlib.util,tempfile,unittest
ROOT=Path(__file__).resolve().parents[1]
class ManualInstaller(unittest.TestCase):
 def module(self):
  p=ROOT/'tools/install_sd.py';self.assertTrue(p.exists(),'manual installer missing')
  spec=importlib.util.spec_from_file_location('install_sd',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
 def test_copy_templates_and_directories(self):
  m=self.module()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);src=root/'src';dst=root/'dst';(src/'lab/empty').mkdir(parents=True);(src/'lab/empty/.gitkeep').touch();(src/'lab/key.txt.example').write_text('# blank template\n');(src/'lab/data.bin').write_bytes(b'data')
   result=m.install(src,dst);self.assertEqual(result['copied'],2);self.assertTrue((dst/'lab/empty').is_dir());self.assertFalse((dst/'lab/empty/.gitkeep').exists());self.assertEqual((dst/'lab/key.txt').read_text(),'# blank template\n');self.assertFalse((dst/'lab/key.txt.example').exists());self.assertEqual((dst/'lab/data.bin').read_bytes(),b'data')
 def test_existing_files_and_symlinks_are_not_overwritten(self):
  m=self.module()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);src=root/'src';dst=root/'dst';src.mkdir();dst.mkdir();(src/'key.txt.example').write_text('# blank\n');(dst/'key.txt').write_text('private value');m.install(src,dst);self.assertEqual((dst/'key.txt').read_text(),'private value');(dst/'key.txt').unlink();(dst/'key.txt').symlink_to(root/'missing');m.install(src,dst);self.assertFalse((root/'missing').exists())
 def test_reject_destination_within_source(self):
  m=self.module()
  with tempfile.TemporaryDirectory() as d:
   src=Path(d)
   for dst in [src,src/'nested']:
    with self.assertRaises(ValueError):m.install(src,dst)
class InstallerTraversalAndPrecedence(unittest.TestCase):
 module=ManualInstaller.module
 def test_destination_subdirectory_symlink_does_not_escape_card(self):
  m=self.module()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);src=root/'src';dst=root/'dst';outside=root/'outside'
   (src/'lab').mkdir(parents=True);dst.mkdir();outside.mkdir()
   (src/'lab/seed.cfg.example').write_text('blank');(dst/'lab').symlink_to(outside,target_is_directory=True)
   m.install(src,dst);self.assertEqual(list(outside.iterdir()),[])
 def test_real_assets_precede_templates_and_source_symlinks_are_skipped(self):
  m=self.module()
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);src=root/'src';dst=root/'dst';src.mkdir()
   (src/'config.cfg').write_text('safe asset');(src/'config.cfg.example').write_text('blank')
   (src/'linked').symlink_to(src/'config.cfg');m.install(src,dst)
   self.assertEqual((dst/'config.cfg').read_text(),'safe asset');self.assertFalse((dst/'linked').exists())
if __name__=='__main__':unittest.main()

