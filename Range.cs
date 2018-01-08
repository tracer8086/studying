using System;
using System.Collections;
using System.Collections.Generic;

namespace AlgorithmTools
{
    public class Range : IEnumerable<int>
    {
        // Fields of range: [from; to).
        private int from;
        private int to;
        private int delta;

        // Range limits are incapsulated in properties to prevent situation when From > To or To < From.
        public int From
        {
            get => from;
            set => from = value;
        }

        public int To
        {
            get => to;
            set => to = value;
        }

        // Delta is the counting offset. It denotes difference between two nearby elements.
        public int Delta
        {
            get => delta;

            set
            {
                if (value == 0)
                    throw new ArgumentException("Delta must be non-zero.");

                delta = value;
            }
        }

        // Current value of counter; it is set to from value before counting.
        public int Current { get; set; }
        
        public Range(int to)
        {
            To = to;
            Current = From = 0;
            Delta = 1;
        }

        public Range(int from, int to, int delta = 1)
        {
            To = to;
            Current = From = from;
            Delta = delta;
        }

        // Counting.
        public IEnumerator<int> GetEnumerator()
        {
            for (Current = from; Current < to; Current += Delta)
                yield return Current;
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}
