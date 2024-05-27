from functools import partial
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QAction


class RecentItemsList:
	"""
	Use for filling item files, (or other things).
	The most item selected is always returned first in the list.
	Maximum length is enforced.
	Items may be removed, such as when a file is missing.
	"""

	def __init__(self, items):
		self.items = items

	def select(self, item):
		"""
		Shifts the given item to the top of the list
		"""
		old_items = self.items
		self.items = [item]
		self.items.extend([old_item for old_item in old_items if old_item != item])

	def remove(self, item):
		self.items = [old_item for old_item in self.items if old_item != item]

	@pyqtSlot()
	def fill_menu(self, menu, trigger_function):
		"""
		Convenience function for PyQt when "aboutToShow" is triggered.

			self.menuOpen_Recent.aboutToShow.connect(self.fill_recent_files)

		Pass a form's menu object as the first parameter.

		The "trigger_function" is a method in your window class which is called when
		the user makes a selection. The callback is passed the value of the item
		selected.
		"""
		menu.clear()
		actions = []
		for item in self.items:
			action = QAction(item, self)
			action.triggered.connect(partial(trigger_function, item))
			actions.append(action)
		menu.addActions(actions)

