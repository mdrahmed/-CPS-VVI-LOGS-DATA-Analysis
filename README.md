Working files,

`hbw-fetch5.txt` file is contains the `loaded values`, but this is printing the address, not the real content of the values.

`hbw-fetch6.txt` contains some zeroes but those are wp[i][j] zeroes.

`hbw-fetch7.txt` contains following data about the workpieces,
```
Function: _ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv
Condition true block: 1
Condition true block: 1
loaded values: 2137910232
Condition false block: 0
Condition true block: 1
loaded values: 2137903760
Condition false block: 0
Condition true block: 1
loaded values: 2137894424
Condition false block: 0
Condition false block: 0
Condition true block: 1
Condition true block: 1
loaded values: 2137910352
Condition false block: 0
Condition true block: 1
loaded values: 2137910312
Condition false block: 0
Condition true block: 1
loaded values: 2137910272
Condition false block: 0
Condition false block: 0
Condition true block: 1
Condition true block: 1
loaded values: 2137910472
Condition false block: 0
Condition true block: 1
loaded values: 2137910432
Condition false block: 0
Condition true block: 1
loaded values: 2137910392
Condition false block: 0
Condition false block: 0
Condition false block: 0
loaded values: -1
loaded values: -1
Function: _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E
Condition false block: 0
Called from: _ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values: 0
Condition false block: 0
Called from: _ZN2ft19TxtHighBayWarehouse14fetchContainerEv _ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv callInst_values: 0
```


### Detection of the changed data
`hbw-fetch8-ch.txt` contains following data, it stores when the `A1` is set to `null`,
```
Function: _ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv
Condition true block: 1
Condition true block: 1
loaded values: 2137903760
Condition false block: 0
Condition true block: 1
loaded values: 2137894424
Condition false block: 0
Condition true block: 1
loaded values: 0
Condition true block: 1
Condition false block: 0
Condition false block: 0
Condition false block: 0
loaded values: 0
loaded values: 0
Function: _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E
Condition true block: 1
Condition false block: 0
Called from: _ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv _ZN2ft26TxtHighBayWarehouseStorage10isValidPosENS_11StoragePos2E callInst_values: -1
Condition true block: 1
loaded values: 0
loaded values: 0
loaded values: 2137708872
loaded values: 2137049476
Function: _ZN2ft15SubjectObserver6NotifyEv
```

I set the space `A1` to `null` and the coordinates of this position is `0,0` . And the loop will start running from the `0,2`,`0,1`,`0,0`.
And in the log, after the `_ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv` function is called, we can see the 3rd loaded values is zero,
```
Function: _ZN2ft26TxtHighBayWarehouseStorage14fetchContainerEv
Condition true block: 1
Condition true block: 1
loaded values: 2137903760
Condition false block: 0
Condition true block: 1
loaded values: 2137894424
Condition false block: 0
Condition true block: 1
loaded values: 0
```
And as it found 1 empty stop, the loop is supposed to stop running according to the code,
```
	for(int i=0;i<3 && !found;i++)
	{
		for(int j=2;j>=0&& !found;j--)
		{
			StoragePos2 p;
			p.x = i; p.y = j;
			//std::cout<<"wp[i][j]: "<<wp[i][j]->state<<"\n";
			if (wp[i][j] == 0)
			{
				SPDLOG_LOGGER_DEBUG(spdlog::get("console"), "cont -> nextFetchPos {} {}",p.x, p.y);
				nextFetchPos = p;
				found = true;
			}
		}
	}
	if (isValidPos(nextFetchPos))
	{
		SPDLOG_LOGGER_DEBUG(spdlog::get("console"), "OK -> nextFetchPos cont ",0);
		wp[nextFetchPos.x][nextFetchPos.y] = 0;
		Notify();
		print();
		return true;
	}
	return false;
}
```
We can also see `isValidPos` function is called after the 3rd value but after getting the loading values of `nextFetchPos = p;` and `found = true;`. So, this log is correctly getting all the data.


`hbw-fetch9-ch.txt` and `hbw-fetch10-ch.txt` is used to check if the spaces were supposed to be read from `2,0`, `1,0`, `0,0`
Because when the storage was full then from `hbw-fetch7.txt`, we got this order, run `Analysis/table.py`,
Loaded values from fetch7.txt:
['2137910232', '2137903760', '2137894424', '2137910352', '2137910312', '2137910272', '2137910472', '2137910432', '2137910392']

But when I made `A1` empty then I got this order,
Loaded values from fetch8-ch.txt:
['2137903760', '2137894424', '0']

**Why the 1st value '2137910232' is missing. It is not missing instead those values are not fixed. It is printing a random data from `2,0` then `1,0` then it finds the `0,0` is empty.**





