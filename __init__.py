#  recent_items_list/__init__.py
#
#  Copyright 2024 liyang <liyang@veronica>
#
from functools import partial


class RecentItemsList:
	"""
	A list which is ordered by the most recently selected item.
	Items may be removed, such as when a file is missing.

	Example:

	in __init__:

		self._recent_files = RecentItemsList(self.settings.value("recent_files", defaultValue=[]))
		self.menuOpen_Recent.aboutToShow.connect(self.fill_recent_files)

	Filling a menu:

		@pyqtSlot()
		def fill_recent_files(self):
			self.menuOpen_Recent.clear()
			actions = []
			for filename in self._recent_files:
				action = QAction(filename, self)
				action.triggered.connect(partial(self.load_soundfont, filename))
				actions.append(action)
			self.menuOpen_Recent.addActions(actions)


	When item is found:

		self._recent_files.select(filename)

	When item is missing:

		self._recent_files.remove(filename)

	Save:

		self.settings.setValue("recent_files", self._recent_files.items)

	"""

	maxlen = 10

	def __init__(self, items):
		self.items = items

	def select(self, item):
		"""
		Insert the given item to the top of the list.
		If the given item already exists, shifts the given item to the top.
		"""
		old_items = self.items
		self.items = [item]
		self.items.extend( old_item for old_item in old_items if old_item != item )
		if self.maxlen > 0:
			self.items = self.items[:self.maxlen]

	def remove(self, item):
		self.items = [old_item for old_item in self.items if old_item != item]

	def __iter__(self):
		return self.items.__iter__()

	def __len__(self):
		return self.items.__len__()


#  end recent_items_list/__init__.py
